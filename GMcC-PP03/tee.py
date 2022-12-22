import sys

class Tee(object):
  def __init__(self, *files):
    self.files = files
  def write(self, obj):
    for f in self.files:
      f.write(obj)
      f.flush() # If you want the output to be visible immediately
  def flush(self) :
    for f in self.files:
      f.flush()

f = open('out.txt', 'w')
original = sys.stdout
sys.stdout = Tee(sys.stdout, f)
print ("test")  # This will go to stdout and the file out.txt

#use the original
sys.stdout = original
print ("This won't appear on file")  # Only on stdout
f.close()