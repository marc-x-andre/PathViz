from typing import Dict

from utils.logger import get_logger


class EventEmitter:

    def __init__(self):
        self.logger = get_logger(__name__)
        self._callbacks: Dict[str, callable] = {}

    def on(self, event_name, function):
        self._callbacks[event_name] = self._callbacks.get(event_name, []) + [function]
        return function

    def emit(self, event_name, **kwargs):
        self.logger.info(f"Event '{event_name.name}'", **kwargs)
        [function(**kwargs) for function in self._callbacks.get(event_name, [])]

    def off(self, event_name, function):
        self._callbacks.get(event_name, []).remove(function)

