from enum import Enum

from dbm.db_manager import DBManager
from utils.event_emitter import EventEmitter


class Event(Enum):
    REGENERATE_GRAPH = 1
    NEW_GRAPH = 2


class _Common:

    gui_event = EventEmitter()
    db_manager = DBManager()


Common = _Common()
