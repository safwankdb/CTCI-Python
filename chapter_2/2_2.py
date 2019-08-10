'''
- Title: Return Kth to last
- Problem: Implement an algorithm to find the kth to last element of a singly linked list.
- Authors: Mohd Safwan, 
'''

# Recursive Solution
def nth_to_last(head, k, i):
    if head is None:
        return None
    nd = nth_to_last(head.next, k, i)
    i[0] = i[0] + 1
    if i[0]==k:
        return head
    return nd

def nth_to_last_driver(head, k):
    i = [0]
    return nth_to_last(head, k, i)

# Iterative Solution
def nth_to_last1(head, k):
    p1 = head
    p2 = head
    for _ in range(k):
        if p1 is None:
            return None
        p1 = p1.next
    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return p2
