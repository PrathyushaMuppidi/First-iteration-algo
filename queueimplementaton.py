
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.insert(0,new_element)
        pass

    def peek(self):
        return self.storage[-1]
        pass 

    def dequeue(self):
        return self.storage.pop(-1)
        pass
    
