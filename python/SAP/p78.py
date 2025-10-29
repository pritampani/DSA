#Find middle element


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def find_middle(self,head):
        slow=head
        fast=head
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        return slow.data
    

# Helper to build a linked list
def build_list(values):
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        curr.next = Node(v)
        curr = curr.next
    return head

head = build_list([1, 2, 3, 4, 5])
s = Solution()
print(s.find_middle(head))

head2 = build_list([1, 2, 3, 4, 5, 6])
print(s.find_middle(head2))