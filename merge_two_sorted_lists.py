from linkedlist import Node
from linkedlist import LinkedList

class LinkedListMerger():
     def mergeTwoLists(self, list1, list2):

        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        temp = Node(None)

        if list1.data <= list2.data:
            temp = list1
            temp.next = self.mergeTwoLists(list1.next, list2)
        else:
            temp = list2
            temp.next = self.mergeTwoLists(list2.next, list1)
        
        return temp

llm = LinkedListMerger()

ll1 = LinkedList()
ll1.append(1)
ll1.append(2)
ll1.append(3)
print(f"linked list 1: {ll1}") # (1) -> (2) -> (3) -> 

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)
print(f"linked list 2: {ll2}") # (2) -> (4) -> (6) -> 

merged_list = LinkedList()
merged_list.head = llm.mergeTwoLists(ll1.head,ll2.head)

print(f"merged list: {merged_list}") # (1) -> (2) -> (2) -> (3) -> (4) -> (6) -> 

ll1 = LinkedList()
ll1.append(0)

ll2 = LinkedList()

merged_list2 = LinkedList()
merged_list2.head = llm.mergeTwoLists(ll1.head,ll2.head)

print(merged_list2)

ll1 = LinkedList()

ll2 = LinkedList()

merged_list3 = LinkedList()
merged_list3.head = llm.mergeTwoLists(ll1.head,ll2.head)

print(merged_list3)