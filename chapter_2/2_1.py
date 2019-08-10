'''
- Title: Remove Dups
- Problem: Write code to remove duplicates from an unsorted linked list.
- Follow up: How would you solve this problem if a temporary buffer is not allowed?
- Authors: Mohd Safwan, 
'''

def delete_dups(n):
    # O(n) implementation using hash table
    hash_table = set()
    previous = None
    while n is not None:
        if n.data in hash_table:
            previous.next = n.next
        else:
            hash_table.add(n.data)
            previous = n.next
        n = n.next

def delete_dups2(head):
    # O(n^2) implementation without using buffer
    current = head
    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
