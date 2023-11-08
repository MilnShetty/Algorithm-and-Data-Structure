from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, data):
        self.queue1.append(data)

    def pop(self):
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        popped_element = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return popped_element

stack = StackUsingQueues()

stack.push(1)
stack.push(2)
stack.push(3)


print("Popped:", stack.pop())  
print("Popped:", stack.pop()) 


stack.push(4)
stack.push(5)


print("Popped:", stack.pop())  
print("Popped:", stack.pop()) 
