# main.py

import time
from transitions.extensions import HierarchicalMachine as Machine
from transitions import MachineError

from fsm.config import states, transitions
from fsm.model import GameModel
from library.capture import capture_screenshot
from global_variables import adb_device_id, screenshot_path

def main():
    # 1) Create model & machine
    model = GameModel()
    machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents')
    # machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents_Match')  
    # 2) Main loop
    while True:
        # Capture the screenshot (optional)
        capture_screenshot(adb_device_id, screenshot_path)
        print("=====================================")
        print(f"Current state: {model.state}")
        # Now do tasks based on the current state
        if model.state == 'LiveEvents_PreMatch':
            model.on_enter_LiveEvents_PreMatch()
        elif model.state == 'LiveEvents_Match':
            model.on_enter_LiveEvents_Match()        
        # Sleep a bit and repeat
        time.sleep(2)


if __name__ == "__main__":
    main()
