from d11_part1 import Seats, simulate_till_stabilize
from itertools import product


class NewSeats(Seats):
    DEFAULT_NUMBER_OF_TOLERATED_NEIGHBOURS = 4

    def occupied_neighbours(self, i, j):
        """
        Returns the number of occupied neighbours of seat i, j.
        >>> seats = NewSeats([".##.##.", "#.#.#.#", "##...##", "...L...", "##...##", "#.#.#.#", ".##.##."])
        >>> seats.occupied_neighbours(3, 3)
        0
        >>> seats = NewSeats([".......#.", "...#.....", ".#.......", ".........", "..#L....#", "....#....", ".........", "#........", "...#....."])
        >>> seats.occupied_neighbours(4, 3)
        8
        """  # pylint: disable=line-too-long
        count = 0
        for di, dj in product([-1, 0, 1], repeat=2):
            if (di, dj) == (0, 0):
                continue
            ni, nj = i + di, j + dj
            while 0 <= ni < self.len_x and 0 <= nj < self.len_y:
                if self.is_occupied(ni, nj):
                    count += 1
                    break
                if self.is_free(ni, nj):
                    break
                ni, nj = ni + di, nj + dj
        return count


def main():
    """
    >>> simulate_till_stabilize(NewSeats(["L.LL.LL.LL", "LLLLLLL.LL", "L.L.L..L..", "LLLL.LL.LL", "L.LL.LL.LL", "L.LLLLL.LL", "..L.L.....", "LLLLLLLLLL", "L.LLLLLL.L", "L.LLLLL.LL"])).count_occupied()
    26
    """
    with open("d11_input.txt") as f:
        data = f.read().splitlines()

    print(simulate_till_stabilize(NewSeats(data)).count_occupied())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
