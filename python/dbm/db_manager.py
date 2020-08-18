from contextlib import contextmanager
from typing import Generator, List

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker, Session

from commons.settings import Settings
from dbm.models import Base, SeedInfo, SeedInfoDBModel


@contextmanager
def session_scope(session: Session) -> Generator[Session, None, None]:
    """Provide a transactional scope around a series of operations."""
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


class DBManager:

    def __init__(self, db_url: str = Settings.db_url):
        self._main_engine = create_engine(db_url)
        self._session_factory = orm.scoped_session(sessionmaker())
        self._session_factory.configure(bind=self._main_engine)
        Base.metadata.create_all(self._main_engine)

    def save_seed_info(self, seed_info: SeedInfo):
        with session_scope(self._session_factory()) as session:
            session.merge(seed_info.to_db_model())

    def get_all_seed_info(self) -> List[SeedInfo]:
        with session_scope(self._session_factory()) as session:
            session: Session = session
            return session.query(SeedInfoDBModel).all()

