from model.user import User
from database.database import SessionLocal

class ControllerUser:

    @classmethod
    def register_login(cls, email: str, password: str):
        session = SessionLocal()
        try:
            existing_user = session.query(User).filter_by(email=email).first()
            if existing_user:
                return {"erro":"Usuário já cadastrado"}
            
            new_user = User(
                email = email,
                password = password
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
            
            if user.password != password:
                return {"erro": "Senhas erradas, por favor tente novamente!"}
            
            return {"mensagem": "Login realizado com sucesso!"}
        
        finally:
            session.close()
