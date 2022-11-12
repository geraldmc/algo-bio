import math
import random
import argparse

class Point:
    """
    Data structure for x,y points in a 2d plane.
    """
    def __init__(self, x, y): 
        self.x = x 
        self.y = y
    def __repr__(self):
        return f"Point({self.x},{self.y})" 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __hash__(self):
        return hash((self.x, self.y))
    def __iter__(self): # convert to tuple
        for i in [self.x, self.y]:
          yield i

def get_path(path, i, j, n):
  """ Used by LBP() to print out the final path.
  """
  if n < 0:
    return []
  if i <= j:
    k = path[i][j]
    print(k)
    return [k] + get_path(path, k, j, n-1)
  else:
    k = path[j][i]
    return get_path(path, i, k, n-1) + [k]
    #print(k)

# Parse command line for the points.
def coords(s):
  """ Parse the command line for x,y integers.
  See: https://stackoverflow.com/questions/21519203/plotting-a-list-of-x-y-coordinates-in-matplotlib
  """
  try:
      x, y = map(int, s.split(','))
      return x, y
  except:
      raise argparse.ArgumentTypeError(\
        "Coordinates must be entered x,y `space` x,y `space` ...")

def dist(p1, p2):
  ''' Returns distance between two x,y points. 
  '''
  return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

# Sort an array of points by X coordinate. 
def sortX(points):
  """ Sort an array of points by X coordinate.
  """
  Sx = sorted(points, key=lambda X: [X.x])
  return Sx

def init_matrix(n, val):
  """ A matrix to memoize intermediate steps.
  """
  m = [[val for i in range(n)] for i in repeat(None, n)]
  return m

def LBP1(sp):
  """ A 'bottom-up' solution for shortest bitonic path.
      Expects an array of n points, sorted by x-value.
  """
  n = len(sp)
  DP = init_matrix(n, _inf) # inits to infinity
  path = init_matrix(n, _m1) # inits to -1
  DP[n-2][n-1] = dist(sp[n-2], sp[n-1])
  path[n-2][n-1] = n-1

  for i in range(n-3,-1,-1):
    min = _inf
    for k in range(i+2,n):
      #print(i,k)
      if min > DP[i+1][k] + dist(sp[i], sp[k]):
        min = DP[i+1][k] + dist(sp[i], sp[k])
        mink = k
    # - end first inner for

    DP[i][i+1] = min
    path[i][i+1] = mink
    for j in range(i+2,n):
      DP[i][j] = DP[i+1][j] + dist(sp[i], sp[i+1])
      path[i][j] = i+1
    # - end second inner for
  
  #get_tsp_path(path, i, j, n) # FIXME
  
  # - end outer for loop
  DP[0][0] = DP[0][1] + dist(sp[0], sp[1])
  path[0][0] = 1
  return DP, path

def LBP2(sp):
  """ A 'bottom-up' solution for shortest bitonic path.
      Expects an array of n points, sorted by x-value.
      Returns the length of the shortest path.
  """
  n = len(sp)
  DP = init_matrix(n, _inf) # inits to infinity
  DP[n-2][n-1] = dist(sp[n-2], sp[n-1])

  for i in range(n-3,-1,-1):
    min = _inf
    for k in range(i+2,n):
      #print(i,k)
      if min > DP[i+1][k] + dist(sp[i], sp[k]):
        min = DP[i+1][k] + dist(sp[i], sp[k])
        mink = k
    # - end first inner for

    DP[i][i+1] = min
    for j in range(i+2,n):
      DP[i][j] = DP[i+1][j] + dist(sp[i], sp[i+1])
    # - end second inner for
  
  #get_tsp_path(path, i, j, n) # FIXME
  
  # - end outer for loop
  DP[0][0] = DP[0][1] + dist(sp[0], sp[1])
  return DP

if __name__ == '__main__':
  """ Driver.
  """
  from itertools import repeat
  _inf = float('inf')
  _m1  = -1
  
  parser = argparse.ArgumentParser(description='Bitonic Traveling Salesman Problem (Bitonic TSP).')
  parser.add_argument('--coords', '-c', help="x,y coordinates, separated by space.", 
                          dest="coord", type=coords, nargs='+')
  args = parser.parse_args()

  points = []
  for idx in range(len(args.coord)):
    points.append(Point(args.coord[idx][0], args.coord[idx][1]))

  sp = sortX(points) # sort points along x axis
  D1, path = LBP1(sp)
  D2 = LBP2(sp)
  lbp_rounded1 = round(D1[0][0], 6)
  lbp_rounded2 = round(D2[0][0], 6)

  print('Least Bitonic Path (LBP1): {}.'.format(lbp_rounded1))
  print('Least Bitonic Path (LBP2): {}.'.format(lbp_rounded2))