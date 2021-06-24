from collections import deque # import deque from collection module
# collections name of module
# deque is a class

# wrap list in deque object, "call dq?" and pass empty list as an argument
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft() # remove object from beginning of queue
#popleft method not in lists objects

print(queue)
if not queue: # check if queue is empty by using the not operator
  print("empty")


# stacks, last in, last out, LILO
# first in, first out, FIFO
# queue, remove items from beginning of list, all other shift to left...
# items moved in memeber, use a deque object