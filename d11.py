from itertools import product


class Seats:
    DEFAULT_NUMBER_OF_TOLERATED_NEIGHBOURS = 3

    def __init__(self, seats, number_of_tolerated_neighbours=None):
        self.seats = seats
        self.len_x, self.len_y = len(seats), len(seats[0])
        if number_of_tolerated_neighbours is None:
            self.number_of_tolerated_neighbours = self.DEFAULT_NUMBER_OF_TOLERATED_NEIGHBOURS
        else:
            self.number_of_tolerated_neighbours = number_of_tolerated_neighbours

    def is_occupied(self, i, j):
        """
        Checks if given seat exists and is occupied
        >>> seats = Seats([['#', '.', '#', '#', '.', 'L', '#', '.', '#', '#'], ['#', 'L', '#', '#', '#', 'L', 'L', '.', 'L', '#'], ['L', '.', '#', '.', '#', '.', '.', '#', '.', '.'], ['#', 'L', '#', '#', '.', '#', '#', '.', 'L', '#'], ['#', '.', '#', '#', '.', 'L', 'L', '.', 'L', 'L'], ['#', '.', '#', '#', '#', 'L', '#', '.', '#', '#'], ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'], ['#', 'L', '#', '#', '#', '#', '#', '#', 'L', '#'], ['#', '.', 'L', 'L', '#', '#', '#', 'L', '.', 'L'], ['#', '.', '#', 'L', '#', '#', '#', '.', '#', '#']])
        >>> seats.is_occupied(-1, 0)
        False
        >>> seats.is_occupied(0, 1123412342340)
        False
        >>> seats.is_occupied(1, 2)
        True
        """  # pylint: disable=line-too-long
        return (0 <= i < self.len_x and 0 <= j <
                self.len_y and self.seats[i][j] == '#')

    def is_free(self, i, j):
        return (0 <= i < self.len_x and 0 <= j <
                self.len_y and self.seats[i][j] == 'L')

    def occupied_neighbours(self, i, j):
        """
        Returns the number of occupied neighbours of seat i, j.
        >>> seats = Seats([['#', '.', '#', '#', '.', 'L', '#', '.', '#', '#'], ['#', 'L', '#', '#', '#', 'L', 'L', '.', 'L', '#'], ['L', '.', '#', '.', '#', '.', '.', '#', '.', '.'], ['#', 'L', '#', '#', '.', '#', '#', '.', 'L', '#'], ['#', '.', '#', '#', '.', 'L', 'L', '.', 'L', 'L'], ['#', '.', '#', '#', '#', 'L', '#', '.', '#', '#'], ['.', '.', '#', '.', '#', '.', '.', '.', '.', '.'], ['#', 'L', '#', '#', '#', '#', '#', '#', 'L', '#'], ['#', '.', 'L', 'L', '#', '#', '#', 'L', '.', 'L'], ['#', '.', '#', 'L', '#', '#', '#', '.', '#', '#']])
        >>> seats.occupied_neighbours(4, 5)
        4
        >>> seats.occupied_neighbours(9, 1)
        3
        >>> seats.occupied_neighbours(2, 3)
        7
        >>> seats.occupied_neighbours(1, 2)
        4
        """  # pylint: disable=line-too-long
        count = 0
        for di, dj in product([-1, 0, 1], repeat=2):
            if (di, dj) == (0, 0):
                continue
            if self.is_occupied(i + di, j + dj):
                count += 1
        return count

    def next_occupation(self, i, j):
        """
        Calculates the occupation of the seat in the next step.
        """
        if self.seats[i][j] == 'L' and self.occupied_neighbours(i, j) == 0:
            return '#'
        if self.seats[i][j] == '#' and not (
            self.occupied_neighbours(
                i, j) <= self.number_of_tolerated_neighbours):
            return 'L'
        return self.seats[i][j]

    def one_step(self):
        """
        Performs one simplation step and returns information if the situation changed.
        """
        new_seats = [[self.next_occupation(i, j) for j in range(
            self.len_y)] for i in range(self.len_x)]
        changed = new_seats != self.seats
        self.seats = new_seats
        return changed

    def count_occupied(self):
        """
        Counts the number of occupied seats.
        """
        return sum(map(lambda l: sum(map(lambda x: x == '#', l)), self.seats))


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


def simulate_till_stabilize(simulation: Seats) -> Seats:
    while simulation.one_step():
        pass
    return simulation


def main():
    with open("inputs/d11.txt") as f:
        data = f.read().splitlines()

    print(simulate_till_stabilize(Seats(data)).count_occupied())
    print(simulate_till_stabilize(NewSeats(data)).count_occupied())


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()
