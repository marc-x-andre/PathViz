from enum import Enum

from dbm.db_manager import DBManager
from models.event_emitter import EventEmitter


class Event(Enum):
    CLEAR = "clear"
    RESOLVE_PATH = "resolve_path"
    NEW_GRAPH = ""


class _Common:
    """
    Singleton service/object use in the whole application
    """

    gui_event = EventEmitter()
    algorithm_event = EventEmitter()
    db_manager = DBManager()


Common = _Common()
