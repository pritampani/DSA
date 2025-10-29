#Detect loop in linked list

#Reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def detect_loop(self,head):
        slow=head
        fast=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Create a loop: 5 -> 3
head.next.next.next.next.next = head.next.next

s = Solution()
print(s.detect_loop(head))

