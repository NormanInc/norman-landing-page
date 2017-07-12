
from flask.helpers import get_debug_flag

from misc.app_tools import create_app
from config import ProdConfig, DevConfig


CONFIG = DevConfig if get_debug_flag() else ProdConfig


app = create_app(CONFIG)
