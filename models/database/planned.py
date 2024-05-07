import logging
from sqlalchemy import Column, String, BigInteger, Date, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class DataPlanned(Base):
    __tablename__ = "planned"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    photos = Column(String)
    text = Column(String)
    date = Column(DateTime)
    url_post = Column(String)

    def dict(self):
        return {"id": self.id,
                "photos": self.photos,
                "text": self.text,
                "date": self.date,
                "url_post": self.url_post,
                }


class Planned(BaseDB):
    async def new(self, data_planned: DataPlanned):
        await self._add_obj(data_planned)

    async def get(self, id: int) -> DataPlanned | None:
        result = await self._get_object(DataPlanned, id)
        return result

    async def update(self, data_planned: DataPlanned) -> None:
        await self._update_obj(instance=data_planned, obj=DataPlanned)

    async def delete(self, data_planned: DataPlanned) -> None:
        await self._delete_obj(instance=data_planned)

    async def in_(self, id: int) -> DataPlanned | bool:
        result = await self.get(id)
        if type(result) is DataPlanned:
            return result
        return False
