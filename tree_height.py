import sys
import threading
import numpy as np

def compute_height(root, elements):
  children = np.where(elements == root)[0]
  #print(children)

  # base case: if no children found
  if children.size == 0:
    return 0

  # return the biggest subtree size
  return 1 + max(compute_height(child, elements) for child in children)


def main():
  num = None
  while not num:
    mode = input("Enter input mode (F/I): ")
    
    if mode == "F":
      file = input("Enter filename: ")
      f = open(file, "r")
      num = int(f.readline())
      # use numpy's int8 type to save memory (similar to java's byte type)
      # appears to just work
      elements = np.array(f.readline().split(), dtype=np.int16)
      
    elif mode == "I":
      num = int(input("Enter a number of elements in a tree: "))
      elements = np.array(input("Enter elements: ").split(), dtype=np.int16)
      
    else:
      print("Wrong mode")
      
  if len(elements) != num:
    print("The amount of elements does not match")
    quit()
  
  print(compute_height(-1, elements))

  
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start() # the command is started in a thread, no need to run main() again
