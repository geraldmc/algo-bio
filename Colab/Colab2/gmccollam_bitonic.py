import math
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
  ''' Return the distance between two x,y points. 
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

def BTSP(sp):
  """ A 'bottom-up' DP solution to shortest bitonic path.
      Takes an array of n points, sorted by x-value.
      Returns the length of the shortest bitonic path.
      Index from 0 to n-1.
  """
  _inf = float('inf')
  n = len(sp)
  DP = init_matrix(n, _inf) # inits to infinity
  # init DP to the distance of the last two points in array (n-2, n-1)
  DP[n-2][n-1] = dist(sp[n-2], sp[n-1]) 

  for i in range(n-3,-1,-1):
    min = _inf
    for k in range(i+2,n):
      if min > DP[i+1][k] + dist(sp[i], sp[k]):
        min = DP[i+1][k] + dist(sp[i], sp[k])
    # - end first inner for
    #print('end first inner loop...')
    #print(DP)

    DP[i][i+1] = min
    for j in range(i+2,n):
      DP[i][j] = DP[i+1][j] + dist(sp[i], sp[i+1])
    #print('second loop...')
    #print(DP)
    # - end second inner for

  # - end outer for loop

  DP[0][0] = DP[0][1] + dist(sp[0], sp[1])
  #print('set base case.')
  #print(DP)
  return DP

if __name__ == '__main__':
  """ Driver---------------------------------------------------
  
  Examples: 
  n=3
  >> python gmccollam_bitonic.py -c 0,0 1,1 2,0
  >> Shortest Bitonic Path (SBP): 4.82842712

  n=4
  >> python gmccollam_bitonic.py -c 0,1 1,2 2,0 3,1
  >> Shortest Bitonic Path (SBP): 7.300563

  n=5
  >> python gmccollam_bitonic.py -c 0,0 1,2 2,1 3,2 4,0 
  >> Shortest Bitonic Path (SBP): 10.944272

  """

  from itertools import repeat
  
  parser = argparse.ArgumentParser(description='Bitonic Traveling Salesman Problem (Bitonic TSP).')
  parser.add_argument('--coords', '-c', help="x,y coordinates, separated by space.", 
                          dest="coord", type=coords, nargs='+')
  args = parser.parse_args()

  points = []
  for idx in range(len(args.coord)):
    points.append(Point(args.coord[idx][0], args.coord[idx][1]))

  sp = sortX(points) # sort points along x axis
  D = BTSP(sp)
  #print(D)
  result = round(D[0][0], 6)

  print('Shortest Bitonic Path (SBP): {}.'.format(result))
