from typing import Optional

from pydantic.main import BaseModel
from sqlalchemy import Column, String, BigInteger, Boolean
from sqlalchemy.ext.declarative import declarative_base

from commons.settings import Settings

Base = declarative_base()


class SeedInfoDBModel(Base):
    __tablename__ = "seed_info"

    seed = Column(BigInteger, primary_key=True)
    version = Column(String, primary_key=True, default=Settings.version)
    comment = Column(String)
    aesthetic = Column(Boolean, default=None)
    resolvable = Column(Boolean, default=None)


class SeedInfo(BaseModel):
    seed: int
    version: str = Settings.version
    comment: Optional[bool] = None
    aesthetic: Optional[bool] = None
    resolvable: Optional[bool] = None

    def to_db_model(self):
        return SeedInfoDBModel(
            seed=self.seed,
            version=self.version,
            comment=self.comment,
            aesthetic=self.aesthetic,
            resolvable=self.resolvable,
        )

    @staticmethod
    def from_db_model(model: SeedInfoDBModel):
        return SeedInfo(
            seed=model.seed,
            version=model.version,
            comment=model.comment,
            aesthetic=model.aesthetic,
            resolvable=model.resolvable,
        )

