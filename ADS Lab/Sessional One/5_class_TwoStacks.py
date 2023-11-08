class TwoStacks:
    def __init__(self, N):
        self.N = N
        self.array = [None] * N
        self.top1 = -1
        self.top2 = N 

    def push1(self, data):
        if self.top1 < self.top2 - 1:
            self.top1 += 1
            self.array[self.top1] = data
        else:
            print("Stack 1 is full. Cannot push element.")

    def push2(self, data):
        if self.top1 < self.top2 - 1:
            self.top2 -= 1
            self.array[self.top2] = data
        else:
            print("Stack 2 is full. Cannot push element.")

    def pop1(self):
        if self.top1 >= 0:
            data = self.array[self.top1]
            self.top1 -= 1
            return data
        else:
            print("Stack 1 is empty. Cannot pop element.")
            return None

    def pop2(self):
        if self.top2 < self.N:
            data = self.array[self.top2]
            self.top2 += 1
            return data
        else:
            print("Stack 2 is empty. Cannot pop element.")
            return None


two_stacks = TwoStacks(6)


two_stacks.push1(1)
two_stacks.push1(2)
two_stacks.push1(3)


two_stacks.push2(4)
two_stacks.push2(5)
two_stacks.push2(6)


two_stacks.push1(7)  
two_stacks.push2(7)  


print("Popped from Stack 1:", two_stacks.pop1())
print("Popped from Stack 2:", two_stacks.pop2())


print("Popped from Stack 1:", two_stacks.pop1())
print("Popped from Stack 2:", two_stacks.pop2())
