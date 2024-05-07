import logging
from sqlalchemy import Column, String, BigInteger
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class DateErid(Base):
    __tablename__ = "dates_erid"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    req_id = Column(BigInteger)

    def dict(self):
        return {"id": self.id,
                "req_id": self.req_id,
                }


class DatesErid(BaseDB):
    async def new(self, date_erid: DateErid):
        await self._add_obj(date_erid)

    async def get(self, id: int) -> DateErid | None:
        result = await self._get_object(DateErid, id)
        return result

    async def update(self, date_erid: DateErid) -> None:
        await self._update_obj(instance=date_erid, obj=DateErid)

    async def delete(self, date_erid: DateErid) -> None:
        await self._delete_obj(instance=date_erid)

    async def in_(self, id: int) -> DateErid | bool:
        result = await self.get(id)
        if type(result) is DateErid:
            return result
        return False
