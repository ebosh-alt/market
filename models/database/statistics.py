import logging
from sqlalchemy import Column, String, BigInteger, Float, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class Statistic(Base):
    __tablename__ = "statistics"
    id = Column(BigInteger, primary_key=True)
    document_id = Column(String)
    user_id = Column(BigInteger)
    amount = Column(Float)
    date = Column(DateTime)

    def dict(self):
        return {"id": self.id,
                "document_id": self.document_id,
                "user_id": self.user_id,
                "amount": self.amount,
                "date": self.date,
                }


class Statistics(BaseDB):
    async def new(self, statistic: Statistic):
        await self._add_obj(statistic)

    async def get(self, id: int) -> Statistic | None:
        result = await self._get_object(Statistic, id)
        return result

    async def update(self, statistic: Statistic) -> None:
        await self._update_obj(instance=statistic, obj=Statistic)

    async def delete(self, statistic: Statistic) -> None:
        await self._delete_obj(instance=statistic)

    async def in_(self, id: int) -> Statistic | bool:
        result = await self.get(id)
        if type(result) is Statistic:
            return result
        return False
