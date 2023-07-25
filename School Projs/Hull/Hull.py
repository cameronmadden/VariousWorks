#  File: Hull.py

#  Description:

#  Student Name: Taylor Chhay

#  Student UT EID: tsc899

#  Course Name: CS 313E

#  Unique Number: 52595

#  Date Created: Sep. 26, 2021

#  Date Last Modified: Sep. 27, 2021

import sys

import math

class Point (object):
  # constructor
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

  # get the distance to another Point object
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
    def __eq__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

    def __ne__ (self, other):
        tol = 1.0e-8
        return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

    def __lt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
        else:
            return (self.y < other.y)
        return (self.x < other.x)

    def __le__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y <= other.y)
        return (self.x <= other.x)

    def __gt__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return False
            else:
                return (self.y > other.y)
        return (self.x > other.x)

    def __ge__ (self, other):
        tol = 1.0e-8
        if (abs(self.x - other.x) < tol):
            if (abs(self.y - other.y) < tol):
                return True
            else:
                return (self.y >= other.y)
        return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
    matrix = [[1, p.x, p.y], [1, q.x, q.y], [1, r.x, r.y]]
    # determinant eqt:
    # top left * ( mid * bot right - mid right * bot mid )
    # - top mid * ( mid left * bot right - mid right * bot left )
    # + top right * ( mid left * bot mid - mid * bot left )
    determinant = matrix[0][0] * ( matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1] ) \
                  - matrix[0][1] * ( matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) \
                  + matrix[0][2] * ( matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0] )
    return determinant

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    sorted_points = (sorted(sorted_points , key=lambda k: [k.x, k.y]))
    upper_hull = []
    upper_hull.append(sorted_points[0])
    upper_hull.append(sorted_points[1])
    i = 2
    while i < len(sorted_points):
        upper_hull.append(sorted_points[i])
        while len(upper_hull) >= 3 and det(upper_hull[-1],upper_hull[-2],upper_hull[-3]) < 0:
            upper_hull.remove(upper_hull[-2])
        i+=1
    lower_hull = []
    lower_hull.append(sorted_points[-1])
    lower_hull.append(sorted_points[-2])

    i = len(sorted_points)-3
    while i >= 0:
        lower_hull.append(sorted_points[i])
        while len(lower_hull) >= 3 and det(lower_hull[-1],lower_hull[-2],lower_hull[-3]) < 0:
            lower_hull.remove(lower_hull[-2])
        i-=1
    lower_hull.remove(lower_hull[0])
    lower_hull.remove(lower_hull[-1])
    convex_hull = []
    for i in upper_hull:
        print ("(" + str(i.x) + ", " + str(i.y) + ")")
    for i in lower_hull:
        print ("(" + str(i.x) + ", " + str(i.y) + ")")
    convex_hull = upper_hull + lower_hull

    return convex_hull



# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    n = len(convex_poly)
    add_xy = 0
    add_yx = 0
    
    # list of n points
    for pts in range(n):
        x = convex_poly[pts].x
        if pts == (n - 1):
            y = convex_poly[0].y
        else:
            y = convex_poly[pts + 1].y
 
        add_xy += x * y
        
        y = convex_poly[pts].y

        if pts == (n - 1):
            x = convex_poly[0].x
        else:
            x = convex_poly[pts + 1].x

        add_yx += y * x
                   
    return (1 / 2) * abs((add_xy) - (add_yx))

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

    return "all test cases passed"

def main():
  # create an empty list of Point objects
    points_list = []

  # read number of points
    line = sys.stdin.readline()
    line = line.strip()
    num_points = int (line)

  # read data from standard input
    for i in range (num_points):
        line = sys.stdin.readline()
        line = line.strip()
        line = line.split()
        x = int (line[0])
        y = int (line[1])
        points_list.append (Point (x, y))

  # sort the list according to x-coordinates
    sorted_points = sorted (points_list)

    # prints the sorted list of point objects
#    for p in sorted_points:
#        print(str(p))
  # get the convex hull

  # run your test cases
  # print your results to standard output
  # print the convex hull
    print('Convex Hull')
  # get the area of the convex hull
    area = area_poly(convex_hull (sorted_points))
    print('\nArea of Convex Hull =', area)

  # print the area of the convex hull

if __name__ == "__main__":
    main()


