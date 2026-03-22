# This is part of Python’s type hinting system
# Optional denotes something that could be set to None.
from typing import Optional

import tcod.event
from actions import Action, EscapeAction, MovementAction

# We’re creating a class called EventHandler, which is a subclass of tcod’s EventDispatch class.
# EventDispatch is a class that allows us to send an event to its proper method based on what type of event it is.
class EventHandler(tcod.event.EventDispatch[Action]):

# Here’s an example of us using a method of EventDispatch: ev_quit is a method defined in EventDispatch, which we’re overriding in EventHandler. 
# ev_quit is called when we receive a “quit” event, which happens when we click the “X” in the window of the program. 
# In that case, we want to quit the program, so we raise SystemExit() to do so.
    def ev_quit(self, event : tcod.event.Quit) -> Optional[Action]:
        action: Optional[Action] = None
    
    # This method will receive key press events, and return either an Action subclass, or None, if no valid key was pressed.
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        
        # action is the variable that will hold whatever subclass of Action we end up assigning it to. 
        # If no valid key press is found, it will remain set to None. We’ll return it either way.
        action: Optional[Action] = None
        
        # key holds the actual key we pressed. 
        # It doesn’t contain additional information about modifiers like Shift or Alt, just the actual key that was pressed. 
        # That’s all we need right now.
        key = event.sym
        
        # From there, we go down a list of possible keys pressed
        if key == tcod.event.K_UP:
            action = MovementAction(dx = 0, dy = -1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action