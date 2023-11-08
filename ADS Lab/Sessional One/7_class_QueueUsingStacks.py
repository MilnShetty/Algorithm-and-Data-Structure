class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def insert(self, data):
        self.stack1.append(data)

    def delete(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return None

        return self.stack2.pop()


queue = QueueUsingStacks()


queue.insert(1)
queue.insert(2)
queue.insert(3)


print("Deleted:", queue.delete())
print("Deleted:", queue.delete()) 


queue.insert(4)
queue.insert(5)

print("Deleted:", queue.delete())  
print("Deleted:", queue.delete()) 
