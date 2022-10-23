class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self,data=None):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head  #start the loop from head
        while cur.next!=None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elems=[]
        cur = self.head
        while cur.next!=None:
            cur=cur.next
            elems.append(cur.data)
        print(elems)

    def get(self,index):
        if index>=self.length():
            print( "ERROR: 'Get' Index out of range")
            return None
        cur=self.head
        cur_idx=0
        while True:
            cur=cur.next
            if cur_idx == index:
                return cur.data
            cur_idx+=1
    
    def erase(self,index):
        if index>=self.length():
            print( "ERROR: 'Get' Index out of range")
            return None
        cur=self.head
        cur_idx=0
        while True:
            last_node = cur
            cur=cur.next
            if cur_idx == index:
                last_node.next = cur.next
                return
            cur_idx+=1
    
    def insert(self,index,data):
        if index>=self.length()+1:
            print( "ERROR: 'Get' Index out of range")
            return None
        cur_idx=0
        cur=self.head
        while True:
            last_node=cur
            cur = cur.next
            if cur_idx == index:
                new_node = node(data)
                last_node.next = new_node
                new_node.next = cur
                return
            cur_idx+=1
        



my_list=linked_list()
my_list.display()
my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
print(my_list.get(4))
my_list.erase(3)
my_list.display()
my_list.insert(4,3)
my_list.display()



