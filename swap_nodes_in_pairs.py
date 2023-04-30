from linkedlist import LinkedList

class NodeSwapper():
    def swap_nodes_in_pairs(self, node):
        if node == None or node.next == None:
            return node # base case
        temp1 = node.next
        temp2 = node.next.next
        node.next.next = node
        node.next = temp2
        node = temp1
        node.next.next = self.swap_nodes_in_pairs(node.next.next) # recursive case
        return node

### TEST CODE ###
if __name__ == "__main__":
        
    ns = NodeSwapper()

    ### n items, where n is even ###
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(f"original LL: {ll}")

    swapped_ll = LinkedList()
    swapped = ns.swap_nodes_in_pairs(ll.head)
    swapped_ll.head = swapped
    print(f"Swapped LL: {swapped_ll}")

    ### n items, where n is odd ###
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    print(f"original LL: {ll}")

    swapped_ll = LinkedList()
    swapped = ns.swap_nodes_in_pairs(ll.head)
    swapped_ll.head = swapped
    print(f"Swapped LL: {swapped_ll}")

    ### single item list ###
    ll = LinkedList()
    ll.append(1)
    print(f"original LL: {ll}")

    swapped_ll = LinkedList()
    swapped = ns.swap_nodes_in_pairs(ll.head)
    swapped_ll.head = swapped
    print(f"Swapped LL: {swapped_ll}")

    ### empty list ###
    ll = LinkedList()
    print(f"original LL: {ll}")
    swapped_ll = LinkedList()
    swapped = ns.swap_nodes_in_pairs(ll.head)
    swapped_ll.head = swapped
    print(f"Swapped LL: {swapped_ll}")
