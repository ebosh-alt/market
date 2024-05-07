import logging
from sqlalchemy import Column, String, BigInteger, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class Advertisement(Base):
    __tablename__ = "advertisements"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger)
    photos = Column(String)
    text = Column(String)
    date = Column(DateTime)

    def dict(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "photos": self.photos,
                "text": self.text,
                "date": self.date,
                }


class Advertisements(BaseDB):
    async def new(self, advertisement: Advertisement):
        await self._add_obj(advertisement)

    async def get(self, id: int) -> Advertisement | None:
        result = await self._get_object(Advertisement, id)
        return result

    async def update(self, advertisement: Advertisement) -> None:
        await self._update_obj(instance=advertisement, obj=Advertisement)

    async def delete(self, advertisement: Advertisement) -> None:
        await self._delete_obj(instance=advertisement)

    async def in_(self, id: int) -> Advertisement | bool:
        result = await self.get(id)
        if type(result) is Advertisement:
            return result
        return False
