import logging
from sqlalchemy import Column, String, BigInteger
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True)
    fullname = Column(String)
    organization = Column(String)
    name_organization = Column(String)
    inn = Column(String)
    phone = Column(String)
    email = Column(String)

    def dict(self):
        return {"id": self.id,
                "fullname": self.fullname,
                "organization": self.organization,
                "name_organization": self.name_organization,
                "inn": self.inn,
                "phone": self.phone,
                "email": self.email,
                }


class Users(BaseDB):
    async def new(self, user: User):
        await self._add_obj(user)

    async def get(self, id: int) -> User | None:
        result = await self._get_object(User, id)
        return result

    async def update(self, user: User) -> None:
        await self._update_obj(instance=user, obj=User)

    async def delete(self, user: User) -> None:
        await self._delete_obj(instance=user)

    async def in_(self, id: int) -> User | bool:
        result = await self.get(id)
        if type(result) is User:
            return result
        return False
