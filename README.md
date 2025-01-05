
```markdown
# Project Structure

```plaintext
my_project/
├── main.py
├── fsm/
│   ├── __init__.py
│   ├── config.py            # Contains 'states' list & 'transitions' list
│   └── model.py             # Contains GameModel class
├── library/
│   ├── __init__.py
│   └── capture.py           # Example: capture_screenshot or other utility functions
├── global_variables.py
└── requirements.txt         # Dependencies: transitions, pillow, pytesseract, etc.
```

---

## Key Files and Functionality

### **1. `fsm/config.py` (States & Transitions)**
- Defines the structure of the finite state machine (FSM).
- Includes the `states` and `transitions` lists.
- **Note**: This file **does not** create the machine instance. It serves as the configuration data for the FSM.

---

### **2. `fsm/model.py` (FSM Model Class)**
- Contains the `GameModel` class, which handles FSM logic and transitions.
- Implements methods like `is_LiveEvents_cond()`, used by the `transitions` library as a condition for state transitions.
- Relies on the following imports from `global_variables.py`:
  - `adb_device_id`
  - `screenshot_path`
- Performs ADB taps when specific conditions are met, then returns `True` to allow the transition.

---

### **3. `library/capture.py` (Utility Functions)**
- Provides utility functions like `capture_screenshot` and other helper methods.
- Facilitates interaction with the ADB environment, such as capturing screenshots for processing.

## Example Usage

### Running the Project
Execute the main script:
```bash
python main.py
```

### Key Functionality

- **FSM Structure**: Managed through `fsm/config.py` and `fsm/model.py`.
- **Screenshot Capture**: Use `library/capture.py` for interacting with ADB to take screenshots.
- **Condition Checking**: The `GameModel` class evaluates conditions like `is_LiveEvents_cond()` to perform transitions.
### Addition
- To add more task :
1. Go to file task.py and define
2. Use file find_location.py to see the coordinate
3. Go to file main.py to use


# Appendix
## To change the private DNS settings in BlueStacks to block ad:
```
adb -s emulator-5554 shell settings put global private_dns_mode hostname
adb -s emulator-5554 shell settings put global private_dns_specifier dns.adguard.com
adb -s emulator-5554 shell settings put global private_dns_mode off
```
## To restart ADB 
```
adb kill-server
adb start-server
```
**In short:** I’m using the [**transitions**](https://github.com/pytransitions/transitions) Python library to model a classic automaton (finite state machine). Each **transition** (edge in the automaton) is specified by:

1. **Trigger name** (like `to_match` or `button1`)  
2. **Source state** (where the transition starts)  
3. **Destination state** (where it ends)  
4. (Optional) **Condition(s)** (boolean functions the library checks before allowing the transition)

You then call the trigger method (e.g. `model.to_match()`), and if:

- The **current state** matches the transition's source, and
- The **condition(s)** are satisfied (if any are defined),

the transition occurs (i.e. the machine moves to the destination state). If not, it fails (often raising a `MachineError`), exactly like a classical automaton refusing to transition on certain inputs.
# How to use
review file global_variable to change to the your device name
```mermaid
stateDiagram-v2
    [*] --> LiveEvents
    state LiveEvents {
        [*] --> PreMatch 
        Advertisement --> PreMatch : is_limited_time_offer, is_dream_point_boost, is_champion
        PreMatch --> Match : is_LiveEvents
        Match --> Advertisement : is_champion, is_promotion
        
    }
    LiveEvents --> Career : button 1
    state Career {
        [*] --> CareerPreMatch
        CareerPreMatch --> CareerMatch : is_play_now
        CareerMatch --> CareerPreMatch : 
        
    }
    Career --> LiveEvents : ibutton 2

