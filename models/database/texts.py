import logging
from sqlalchemy import Column, String, BigInteger, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class Text(Base):
    __tablename__ = "texts"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    time = Column(DateTime)
    photos = Column(String)
    text = Column(String)

    def dict(self):
        return {"id": self.id,
                "time": self.time,
                "photos": self.photos,
                "text": self.text
                }


class Texts(BaseDB):
    async def new(self, text: Text):
        await self._add_obj(text)

    async def get(self, id: int) -> Text | None:
        result = await self._get_object(Text, id)
        return result

    async def update(self, text: Text) -> None:
        await self._update_obj(instance=text, obj=Text)

    async def delete(self, text: Text) -> None:
        await self._delete_obj(instance=text)

    async def in_(self, id: int) -> Text | bool:
        result = await self.get(id)
        if type(result) is Text:
            return result
        return False
