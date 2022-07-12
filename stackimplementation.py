def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head:
            temp = self.head
            self.head = new_element
            current = self.head
            current.next = temp
        else:
            self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        current = self.head
        temp = self.head
        if self.head:
            if current.next:
                self.head = current.next
            else:
                self.head = None
            return temp
        else:
            return None
        pass

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        pass
