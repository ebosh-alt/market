import logging
from sqlalchemy import Column, BigInteger, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class CancelTime(Base):
    __tablename__ = "cancel_times"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date = Column(DateTime)

    def dict(self):
        return {"id": self.id,
                "date": self.date,
                }


class CancelTimes(BaseDB):
    async def new(self, cancel_time: CancelTime):
        await self._add_obj(cancel_time)

    async def get(self, id: int) -> CancelTime | None:
        result = await self._get_object(CancelTime, id)
        return result

    async def update(self, cancel_time: CancelTime) -> None:
        await self._update_obj(instance=cancel_time, obj=CancelTime)

    async def delete(self, cancel_time: CancelTime) -> None:
        await self._delete_obj(instance=cancel_time)

    async def in_(self, id: int) -> CancelTime | bool:
        result = await self.get(id)
        if type(result) is CancelTime:
            return result
        return False
