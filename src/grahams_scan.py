"""
Implementation of Graham's Scan based on Java version in:
Algorithms in a Nutshell (G. T. Heineman, G. Pollice, S. Selkow), 2nd Edition, 2016, chapter 3
"""
# graham(P)
#      low = point with lowest y coordinate in P, Ties are broken by selecting the point with lowest x coordinate.
#      remove low from P
#      sort P by descending polar angle with respect to low, P[0] has max polar angle and P[n – 2] has min polar angle
#      hull = {P[n-2], low} # Form hull clockwise starting with min polar angle and low.
#      for i = 0 to n-1 do
#         while (isLeftTurn(secondLast(hull), last(hull), P[i])) do  # Every turn to the left reveals last hull point
#         # must be removed.
#             remove last point in hull
#         add P[i] to hull
#      remove duplicate last point  # Because it will be P[n – 2]
#      return hull
import math


class IPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<IPoint object x: {self.x}, y: {self.y}>"

    def __eq__(self, other):
        """Two IPoints are equal when both x and y are the same"""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """Checks if y coordinate is lower, if the same, checks whether x coordinate is lower"""
        self_smaller = False
        if self.y < other.y:
            self_smaller = True
        elif self.y == other.y:
            if self.x < other.x:
                self_smaller = True
        return self_smaller


class NativeGrahamScan:
    def __init__(self, points: list[IPoint]):
        self.points = points

    def compute(self):
        number_of_points = len(self.points)
        if number_of_points < 3:
            return self.points

        index_lowest = 0
        lowest_point = self.points[0]

        # Find the lowest point
        for i in range(1, number_of_points):
            if self.points[i] < lowest_point:
                lowest_point = self.points[i]
                index_lowest = i

        # Switch the lowest point with the point in the last index
        if index_lowest != (number_of_points - 1):
            tmp_point = self.points[-1]
            self.points[-1] = self.points[index_lowest]
            self.points[index_lowest] = tmp_point

        # TODO: HeapSort and save in sorted_points
        sorted_points = []

        #  Check if all points are collinear, if so, the hull has 2 points and can be returned
        angle_one = math.atan2(sorted_points[0].y - lowest_point.y, sorted_points[0].x - lowest_point.x)
        angle_two = math.atan2(sorted_points[-2].y - lowest_point.y, sorted_points[-2].x - lowest_point.x)
        if angle_one == angle_two:
            return [sorted_points[0], sorted_points[-1]]

        # three points *known* to be on the hull are( in this order) the
        # point with lowest polar angle (sorted_points[n-2]), the lowest point
        # (sorted_points[n - 1]), and the point with the highest polar angle
        # (sorted_points[0]). Start with first two:
        hull = [sorted_points[-1], sorted_points[-2]]

        # Sequentially visit each point in order, removing points upon
        # making mistake. Because we always have at least one "right
        # turn," the inner while loop will always terminate
        for i in range(0, number_of_points - 1):
            while self.is_left_turn(hull[-2], hull[-1], sorted_points[i]):
                hull = hull[:-1]
            hull.insert(0, sorted_points[i])

        return hull[1:]

    def is_left_turn(self, point_one, point_two, point_three):
        return ((point_two.x - point_one.x) * (point_three.y - point_one.y) -
                (point_two.y - point_one.y) * (point_three.x - point_one.x)) > 0


class ReversePolarSorter:
    def __init__(self, base: IPoint):
        self.base_x = base.x
        self.base_y = base.y

    def compare(self, point_one: IPoint, point_two: IPoint):
        """
        Returns -1 if point_one has a larger angle with self.base,
        returns 1 if point_two has a larger angle with self.base
        returns 0 if the points are the same
        """
        if point_one == point_two:
            return 0

        angle_one = math.atan2(point_one.y - self.base_y, point_one.x - self.base_x)
        angle_two = math.atan2(point_two.y - self.base_y, point_two.x - self.base_x)

        if angle_one > angle_two:
            return -1
        elif angle_one < angle_two:
            return 1
        elif angle_one == angle_two:
            if point_one > point_two:
                return -1
            else:
                return 1
