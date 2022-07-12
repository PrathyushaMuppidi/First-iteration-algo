
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        count = 1
        while position>=count:
            if position==count:
                return current
            else:
                current = current.next
                count = count+1
        if position<count:
           return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        count = 1
        while position >=count:
            temp = current
            cnt2 = count +1
            if position==count:
                self.head = new_element
                current = self.head
                current.next = temp
                break
            else: 
                if position==cnt2:
                    current = new_element
                    current.next = temp.next
                    temp.next = current
                    break
                else: 
                    current = current.next
                    count = count + 1
        pass
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        temp = current
        while current.next:
            if value == current.value:
                if self.head:
                    self.head = current.next
                    break
                else:
                    current = temp.next
                    break
            else:
                temp = current
        pass
