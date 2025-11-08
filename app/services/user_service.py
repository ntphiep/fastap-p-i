from sqlalchemy.orm import Session

from app.db.user import User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def list_users(self):
        return self.db.query(User).all()

    def get_user(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, username: str, email: str) -> User:
        new_user = User(username=username, email=email)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user