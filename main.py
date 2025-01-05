# main.py

import time
from transitions.extensions import HierarchicalMachine as Machine
from transitions import MachineError

from fsm.config import states, transitions
from fsm.model import GameModel
from fsm.tasks import is_continue, is_advertisement,is_advertisement_1, is_new_tier, is_forfeits, down_tier
from library.capture import capture_screenshot
from global_variables import adb_device_id, screenshot_path

def main():
    # 1) Create model & machine
    model = GameModel()
    # machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents')
    machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents_Match')  
    # 2) Main loop
    while True:
        # Capture the screenshot (optional)
        capture_screenshot(adb_device_id, screenshot_path)
        print("=====================================")
        print(f"Current state: {model.state}")
        # Try triggers that might cause a state change (if conditions are met)

        # Now do tasks based on the current state
        
        if model.state == 'LiveEvents_PreMatch':
            model.is_LiveEvents_end()
            model.check_tier()
            is_advertisement()
            is_new_tier()

        elif model.state == 'LiveEvents_Match':
            if not model.is_LiveMatch_end():
                model.is_disconnected()
                # if model.tier < 15:
                #     down_tier()
                is_advertisement_1()
                is_forfeits()
                
            
        
        # If you also have tasks for Advertisement, do them here, etc.
        
        # Sleep a bit and repeat
        time.sleep(2)


if __name__ == "__main__":
    main()
