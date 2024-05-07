import logging
from sqlalchemy import Column, String, BigInteger
from .base import Base, BaseDB

logger = logging.getLogger(__name__)


class Signature(Base):
    __tablename__ = "signatures"

    id = Column(BigInteger, primary_key=True)
    r = Column(String)

    def dict(self):
        return {"id": self.id,
                "r": self.r,
                }


class Signatures(BaseDB):
    async def new(self, signature: Signature):
        await self._add_obj(signature)

    async def get(self, id: int) -> Signature | None:
        result = await self._get_object(Signature, id)
        return result

    async def update(self, signature: Signature) -> None:
        await self._update_obj(instance=signature, obj=Signature)

    async def delete(self, signature: Signature) -> None:
        await self._delete_obj(instance=signature)

    async def in_(self, id: int) -> Signature | bool:
        result = await self.get(id)
        if type(result) is Signature:
            return result
        return False
