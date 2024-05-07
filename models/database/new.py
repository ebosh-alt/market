import logging
from sqlalchemy import Column, String, BigInteger
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class DataNew(Base):
    __tablename__ = "new"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    text = Column(String)

    def dict(self):
        return {"id": self.id,
                "text": self.username,
                }


class New(BaseDB):
    async def new(self, data_new: DataNew):
        await self._add_obj(data_new)

    async def get(self, id: int) -> DataNew | None:
        result = await self._get_object(DataNew, id)
        return result

    async def update(self, data_new: DataNew) -> None:
        await self._update_obj(instance=data_new, obj=DataNew)

    async def delete(self, user: DataNew) -> None:
        await self._delete_obj(instance=user)

    async def in_(self, id: int) -> DataNew | bool:
        result = await self.get(id)
        if type(result) is DataNew:
            return result
        return False
