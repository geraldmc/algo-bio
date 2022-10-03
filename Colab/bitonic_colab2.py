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

def get_tsp_path(path, i, j, n):
  """ Used with LBP to print out the final path.
  """
  if n < 0:
    return []
  if i <= j:
    k = path[i][j]
    print(k)
    return [k] + get_tsp_path(path, k, j, n-1)
  else:
    k = path[j][i]
    return get_tsp_path(path, i, k, n-1) + [k]
    #print(k)

# Parse command line for the points.
def coords(s):
  """ Parse the command line for x,y integers.
  """
  try:
      x, y = map(int, s.split(','))
      return x, y
  except:
      raise argparse.ArgumentTypeError(\
        "Coordinates must be entered x,y `space` x,y `space` ...")

def dist(p1, p2):
  ''' This dist function calculates square root.
  '''
  return math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2)

# Sort an array of points by X coordinate. 
def sortX(points):
  """ Sort an array of points by X coordinate.
  """
  Sx = sorted(points, key=lambda X: [X.x])
  return Sx

def init_matrix(n, val):
  d = [[val for i in range(n)] for i in repeat(None, n)]
  return d

def LBP(sp):
  """ Implements shortest bitonic path.
  """
  n = len(sp)
  D = init_matrix(n, _inf) # inits to infinity
  path = init_matrix(n, _m1) # inits to -1
  D[n-2][n-1] = dist(sp[n-2], sp[n-1])
  path[n-2][n-1] = n-1

  for i in range(n-3,-1,-1):
    min = _inf
    for k in range(i+2,n):
      #print(i,k)
      if min > D[i+1][k] + dist(sp[i], sp[k]):
        min = D[i+1][k] + dist(sp[i], sp[k])
        mink = k
    # - end first inner for

    D[i][i+1] = min
    path[i][i+1] = mink
    for j in range(i+2,n):
      D[i][j] = D[i+1][j] + dist(sp[i], sp[i+1])
      path[i][j] = i+1
    # - end second inner for
  
  #get_tsp_path(path, i, j, n)
  
  # - end outer for loop
  D[0][0] = D[0][1] + dist(sp[0], sp[1])
  path[0][0] = 1
  return D, path

if __name__ == '__main__':
  """ Driver for the program.
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
  D, path = LBP(sp)
  lbp_rounded = round(D[0][0], 6)
  print('Length of Least Bitonic Path (LBP): {}.'.format(lbp_rounded))

# https://sandipanweb.wordpress.com/2020/12/08/travelling-salesman-problem-tsp-with-python/
