# main.py

import time
from transitions.extensions import HierarchicalMachine as Machine
from transitions import MachineError
import os
from fsm.config import states, transitions
from fsm.model import GameModel
from library.capture import capture_screenshot
from global_variables import adb_device_id, screenshot_path

def main():
    #Reset the adb server whenever the computer is restarted
    os.system("adb kill-server")
    os.system("adb start-server")
    # 1) Create model & machine
    model = GameModel()
    # machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents_PreMatch')
    machine = Machine(model=model, states=states, transitions=transitions, initial='LiveEvents_Match')
    # machine = Machine(model=model, states=states, transitions=transitions, initial='Career_CareerMatch')
    # machine = Machine(model=model, states=states, transitions=transitions, initial='Career_CareerPreMatch')    
    # 2) Main loop
    while True:
        # Capture the screenshot (optional)
        capture_screenshot(adb_device_id, screenshot_path)
        # print("=====================================")
        # print(f"Current state: {model.state}")
        # Now do tasks based on the current state
        if model.state == 'LiveEvents_PreMatch':
            model.on_enter_LiveEvents_PreMatch()
        elif model.state == 'LiveEvents_Match':
            model.on_enter_LiveEvents_Match()
        elif model.state == 'Career_CareerPreMatch':
            model.on_enter_Career_CareerPreMatch()
        elif model.state == 'Career_CareerMatch':
            model.on_enter_Career_CareerMatch()      
        # Sleep a bit and repeat
        time.sleep(2)


if __name__ == "__main__":
    main()
