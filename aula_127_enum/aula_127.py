from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == '__main__':
    print(move(Directions(Directions.right)))
    print(move(Directions(Directions.left)))
    print(move(Directions(Directions.up)))
    print(move(Directions(Directions.down)))

    print()