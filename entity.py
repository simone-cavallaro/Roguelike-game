from typing import Tuple

class Entity:
    """
    A generic object to represetn players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
    
    def move(self, dx: int, dy: int) -> None:
        """
        Move the entity by a given amount
        """
        self.x += dx
        self.y += dy

#The initializer (__init__) takes four arguments: x, y, char, and color.
#    - x and y are pretty self explanatory: They represent the Entity’s “x” and “y” coordinates on the map.
#    - char is the character we’ll use to represent the entity. Our player will be an “@” symbol, whereas something like a Troll can be the letter “T”.
#    - color is the color we’ll use when drawing the Entity. We define color as a Tuple of three integers, representing the entity’s RGB values.
#    - the other method is move, which takes dx and dy as arguments, and uses them to modify the Entity’s position.        