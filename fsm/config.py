# fsm/config.py

from transitions.extensions import HierarchicalMachine as Machine

# Define hierarchical states
states = [
    {
        'name': 'LiveEvents',
        'initial': 'PreMatch',
        'children': [
            {'name': 'PreMatch'},
            {'name': 'Match'}
        ]
    },
    {
        'name': 'Career',
        'initial': 'CareerPreMatch',
        'children': [
            {'name': 'CareerPreMatch'},
            {'name': 'CareerMatch'}
        ]
    }
]

# Define transitions
transitions = [
    # Top-level transitions
    {'trigger': 'button1',  'source': 'LiveEvents', 'dest': 'Career'},
    {'trigger': 'ibutton2', 'source': 'Career',     'dest': 'LiveEvents'},
    
    # LiveEvents child transitions
    {
        'trigger': 'is_LiveEvents_end',
        'source': 'LiveEvents_PreMatch',
        'dest': 'LiveEvents_Match',
        'conditions': 'is_LiveEvents_end_cond'
    },
    {
        'trigger': 'is_LiveMatch_end',   
        'source': 'LiveEvents_Match', 
        'dest': 'LiveEvents_PreMatch',
        'conditions': 'is_LiveMatch_end_cond'
    },
    {
        'trigger': 'is_disconnected',   
        'source': 'LiveEvents_Match', 
        'dest': 'LiveEvents_PreMatch',
        'conditions': 'is_disconnected_cond'
    },
    # Career child transitions
    {'trigger': 'is_play_now', 'source': 'Career_CareerPreMatch', 'dest': 'Career_CareerMatch'},
    {
        'trigger': 'go_back',
        'source': 'Career_CareerMatch',
        'dest': 'Career_CareerPreMatch'
    },
]
