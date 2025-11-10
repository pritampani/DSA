#Reverse a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def reverseList(self,head):
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev



    def print_list(self,head):
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

s = Solution()
new_head = s.reverseList(head)
s.print_list(new_head)
