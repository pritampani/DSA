# 	Reverse a Linked List – (Coding Section Hand-on) Given a linked list, reverse it. (If allowed)
# Description: Change pointers so that list order is reversed.
# Sample I/O:
# Input list 1->2->3->NULL → Output 3->2->1->NULL.
# Topic: Data Structures – Linked List. Difficulty: Medium. (Fundamental DS problem)



class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class Solution:
    def reverse_linked_list(self,head):
        prev=None
        curr=head

        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev


# Function to print linked list
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else " -> NULL\n")
        curr = curr.next

# Create linked list: 1 -> 2 -> 3 -> NULL
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Original List:")
print_list(head)

# Reverse the list
sol = Solution()
reversed_head = sol.reverse_linked_list(head)

print("Reversed List:")
print_list(reversed_head)