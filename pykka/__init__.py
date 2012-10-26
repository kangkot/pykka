# flake8: noqa
from pykka.exceptions import ActorDeadError, Timeout


#: Pykka's :pep:`386` and :pep:`396` compatible version number
__version__ = '0.16'


def _add_null_handler_for_logging():
    import logging
    try:
        NullHandler = logging.NullHandler  # Python 2.7 and upwards
    except AttributeError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass
    logging.getLogger('pykka').addHandler(NullHandler())

_add_null_handler_for_logging()
