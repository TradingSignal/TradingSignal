import logging
from tradingsignal import version

# define the version before the other imports since these need it
__version__ = version.__version__

from tradingsignal.run_server import run_server

logging.getLogger(__name__).addHandler(logging.NullHandler())
