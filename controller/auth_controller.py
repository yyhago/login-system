from model.user import User
from database.database import SessionLocal
import bcrypt

class ControllerUser:

    @staticmethod # Criptografia da senha
    def hash_password(password: str):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    


    @classmethod
    def register_login(cls, email: str, password: str):
        session = SessionLocal()
        try:
            existing_user = session.query(User).filter_by(email=email).first()
            if existing_user:
                return {"erro":"Usuário já cadastrado"}
            
            hashed_pwd = cls.hash_password(password)
            
            new_user = User(
                email = email,
                password = hashed_pwd
            )

            session.add(new_user)
            session.commit()
            return {"mensagem": "Usuário registrado com sucesso!"}

        except Exception as e:
            session.rollback()
            return {"erro": str(e)}
        finally:
            session.close()

    
    @classmethod
    def login_account(cls, email: str, password: str):
        session = SessionLocal()
        try:
            user = session.query(User).filter_by(email=email).first()
           
            if user is None:
                return {"erro": "Usuário não encontrado"}
            
            if cls.verify_password(password, user.password):
                return {"mensagem": "Login realizado com sucesso!", "user": user.email}
            else:
                return {"erro": "Senha incorreta, por favor tente novamente!"}
            
        except Exception as e:
            return {"erro": str(e)}
        finally:
            session.close()
