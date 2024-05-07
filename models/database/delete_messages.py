import logging
from sqlalchemy import Column, String, BigInteger, DateTime
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class DeleteMessage(Base):
    __tablename__ = "delete_message"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    message_id = Column(BigInteger)

    def dict(self):
        return {"id": self.id,
                "date": self.date,
                "message_id": self.message_id
                }


class DeleteMessages(BaseDB):
    async def new(self, delete_message: DeleteMessage):
        await self._add_obj(delete_message)

    async def get(self, id: int) -> DeleteMessage | None:
        result = await self._get_object(DeleteMessage, id)
        return result

    async def update(self, delete_message: DeleteMessage) -> None:
        await self._update_obj(instance=delete_message, obj=DeleteMessage)

    async def delete(self, delete_message: DeleteMessage) -> None:
        await self._delete_obj(instance=delete_message)

    async def in_(self, id: int) -> DeleteMessage | bool:
        result = await self.get(id)
        if type(result) is DeleteMessage:
            return result
        return False
