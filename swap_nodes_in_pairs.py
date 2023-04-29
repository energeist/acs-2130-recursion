from linkedlist import Node
from linkedlist import LinkedList

class NodeSwapper():
    def swap_nodes_in_pairs(self, node):
        # if node == None or node.next == None:
        #     return node
        # temp1 = node
        # temp2 = node.next
 
        # return node
        
        if node == None or node.next == None:
            return node
        new_head = node.next
        print("\niteration start")
        print(f"node: {node}")
        print(f"node.next: {node.next}")
        temp = node.next.next
        node.next.next = node
        print(f"temp: {temp}")
        node.next = temp
        print("\nafter swapping")
        print(f"node: {node}")
        print(f"node.next: {node.next}")
        if temp:
            node.next.next = self.swap_nodes_in_pairs(node)
        return node
ns = NodeSwapper()

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
# ll.append(5)

print(ll)

swapped_ll = LinkedList()
swapped = ns.swap_nodes_in_pairs(ll.head)
swapped_ll.head = swapped
print(swapped)
print(swapped.next)
print(swapped.next.next)
print(swapped.next.next.next)
print(swapped.next.next.next.next)
# print(swapped_ll)
