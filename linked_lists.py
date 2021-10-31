class node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        if self.next != None:
            next = repr(self.next)
        else:
            next = "none"
        return "node("+str(self.value)+", "+ next +")"

    def __str__(self):
        return str(self.value)
    
class linked_list():
    def __init__(self):
        self.data = None
        self.size = 0

    def add(self, val):
        if self.data == None:
            self.data = node(value=val)
            self.size += 1
        else:
            new_node = node(value=val)
            curr = self.data
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
            self.size += 1

    def __str__(self):
        return self.data.__repr__()

    def __repr__(self):
        return self.data.__repr__()

    def find(self, target, ret_node = False):
        curr = self.data
        i = 0
        if curr.value == target:
            return True, i
        else:
            curr = curr.next
            while curr != None:
                i += 1
                if curr.value == target:
                    return True, i
                curr = curr.next
        return False, -1

    def insert(self, idx, val):
        i = 1
        if i > self.size-1:
            print("Error: can not insert index more than size of list")
        elif i == self.size:
            self.add(val)
        else:
            
            curr = self.data
            new_node = node(val)
            if idx == 0:
                self.data = new_node.next(curr)
                self.size += 1
            else:
                while i != idx:
                    i+=1
                    curr = curr.next
                old_next = curr.next
                new_node.next = old_next
                curr.next = new_node
                self.size += 1

    def delete(self, val):
        found, idx = self.find(val)
        if not found:
            print(str(val)+" is not found.")
        else:
            curr = self.data
            while idx != 0:
                idx -= 1
                prev = curr
                curr = curr.next
            
            prev.next = curr.next
            self.size -= 1


    # def getitem(self, idx):
    #     pass


# class doubly_linked_list():
#     def __init__(self):
#         pass

if __name__ == "__main__":
    l1 = linked_list()
    l1.add(6)
    l1.add(7)
    l1.add(1)
    l1.add(8)
    print(l1)

    print("Is 7 in l1: "+str(l1.find(7)[0]))
    print("Is 5 in l1: "+str(l1.find(5)[0]))
    print("Is 1 in l1: "+str(l1.find(1)[0]))

    l1.insert(2, 20)
    l1.insert(1, 11)
    l1.insert(l1.size, 40)
    print(l1)
    print(l1.size)

    l1.delete(0)
    l1.delete(7)
    print(l1)
    print(l1.size)
    