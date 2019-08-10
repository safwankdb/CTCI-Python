'''
- Title: Delete Middle Node
- Problem: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
- Authors: Mohd Safwan, 
'''

def delete_node(n):
    if n is None or n.next is None:
        return False
    next_node = n.next
    n.data = next_node.data
    n.next = next_node.next
    return True
