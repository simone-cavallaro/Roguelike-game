import tcod
from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler

def main() -> None:
    screen_width = 80
    screen_height = 50

    # We’re placing the player right in the middle of the screen
    #player_x = int(screen_width / 2)
    #player_y = int(screen_height / 2)

    map_width = 80
    map_height = 45

    # Here, we’re telling tcod which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    

    # event_handler is an instance of our EventHandler class. 
    # We’ll use it to receive events and process them
    event_handler = EventHandler()

    # We’re importing the Entity class into main.py, and using it to initialize the player and a new NPC. 
    # We store these two in a set, that will eventually hold all our entities on the map.
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map =game_map, player=player)

    # This part is what actually creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset = tileset,
        title = "SCike",
        vsync = True,
    ) as context:
        # This creates our “console” which is what we’ll be drawing to
        root_console = tcod.Console(screen_width, screen_height, order = "F") # We also set this console’s width and height to the same as our new terminal. 
                                                                              # The “order” argument affects the order of our x and y variables in numpy. 
                                                                              # By default, numpy accesses 2D arrays in [y, x] order, which is fairly unintuitive. 
                                                                              # By setting order="F", we can change this to be [x, y] instead.
        # This is what’s called our ‘game loop’. 
        # Basically, this is a loop that won’t ever end, until we close the screen. Every game has some sort of game loop or another.
        while True:
            engine.render(console=root_console, context=context)
                                                          
            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()

