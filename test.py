import time
from transitions.extensions import HierarchicalMachine as Machine
from transitions import MachineError

from fsm.config import states, transitions
from fsm.model import GameModel
from fsm.tasks import is_continue, is_advertisement,is_advertisement_1, is_new_tier, is_forfeits, fix_state, check_tier
from library.capture import capture_screenshot
from global_variables import adb_device_id, screenshot_path
from main import *
model = GameModel()
model.is_LiveMatch_end()