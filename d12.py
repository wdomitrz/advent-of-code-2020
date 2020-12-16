import numpy as np


movements = {
    'N': np.array([0, 1]),
    'S': np.array([0, -1]),
    'W': np.array([-1, 0]),
    'E': np.array([1, 0])
}


def get_location1(instructions):
    """
    >>> get_location1([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
    array([17, -8])
    """
    angle = 0
    pos = np.zeros(2, dtype=np.int)
    for instr, val in instructions:
        if instr in movements:
            pos += val * movements[instr]
        elif instr == 'R':
            angle -= val
        elif instr == 'L':
            angle += val
        elif instr == 'F':
            pos += val * np.array([int(round(np.cos(np.pi * angle / 180))),
                                   int(round(np.sin(np.pi * angle / 180)))])

    return pos


def get_location2(instructions):
    """
    >>> get_location2([('F', 10), ('N', 3), ('F', 7), ('R', 90), ('F', 11)])
    array([214, -72])
    """
    pos = np.zeros(2, dtype=np.int)
    waypoint = np.array([10, 1])
    for instr, val in instructions:
        if instr in movements:
            waypoint += val * movements[instr]
        elif instr in ['R', 'L']:
            angle = val if instr == 'R' else -val
            rotation = np.array([[int(round(np.cos(np.pi * angle / 180))),
                                  int(round(np.sin(np.pi * angle / 180)))],
                                 [-int(round(np.sin(np.pi * angle / 180))),
                                  int(round(np.cos(np.pi * angle / 180)))]])
            waypoint = rotation @ waypoint
        elif instr == 'F':
            pos += val * waypoint

    return pos


def main():
    with open("inputs/d12.txt") as f:
        data = f.read().splitlines()
    data = list(map(lambda line: (line[0], int(line[1:])), data))

    print(np.abs(get_location1(data)).sum())
    print(np.abs(get_location2(data)).sum())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
