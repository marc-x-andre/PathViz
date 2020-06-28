import inspect

import structlog

structlog.configure(
    processors=[
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.stdlib.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M"),
        structlog.dev.ConsoleRenderer()
    ],
    wrapper_class=structlog.BoundLogger,
    context_class=dict,  # or OrderedDict if the runtime's dict is unordered (e.g. Python <3.6)
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=False
)

_main_logger = structlog.get_logger()


class Logger(structlog.BoundLogger):

    def debug(self, msg, *args, **kwargs):
        pass

    def info(self, msg, *args, **kwargs):
        pass

    def warning(self, msg, *args, **kwargs):
        pass

    def error(self, msg, *args, **kwargs):
        pass

    def exception(self, msg, *args, **kwargs):
        pass

    def bind(self, **kwargs):
        pass


def get_logger(location: str) -> Logger:
    return _main_logger.bind(location=location)


def debug(msg):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])

    get_logger(module.__name__).debug(msg, debug=True, lineno=frame.lineno)


