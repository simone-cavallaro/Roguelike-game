import tcod

def main() -> None:
    screen_width = 80
    screen_height = 50

    # We’re placing the player right in the middle of the screen
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # Here, we’re telling tcod which font to use
    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

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
            root_console.print(x = player_x, y = player_y, string = "@") # This line is what tells the program to actually put the “@” symbol on the screen in its proper place. 
                                                          # We’re telling the root_console we created to print the “@” symbol at the given x and y coordinates.
            # Without this line, nothing would actually print out on the screen. 
            # This is because context.present is what actually updates the screen with what we’ve told it to display so far.
            context.present(root_console)
        

        # This part gives us a way to gracefully exit (i.e. not crashing) the program by hitting the X button in the console’s window.
        # The line for event in tcod.event.wait() will wait for some sort of input from the user (mouse clicks, keyboard strokes, etc.) 
        # and loop through each event that happened. SystemExit() tells Python to quit the current running program.
        for event in tcod.event.wait():
            if event.type == "QUIT":
                raise SystemExit



if __name__ == "__main__":
    main()
