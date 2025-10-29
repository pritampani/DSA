#Merge two sorted linked lists



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Solution:
    def merge_linked(self,h1,h2):
        dummy=Node(0)
        tail=dummy

        while h1 and h2:
            if h1.data<h2.data:
                tail.next=h1
                h1=h1.next
            else:
                tail.next=h2
                h2=h2.next
            tail=tail.next
        if h1:
            tail.next=h1
        else:
            tail.next=h2
        return dummy.next
    


    def print_list(self,head):
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")

# List1: 1 -> 3 -> 5
l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

# List2: 2 -> 4 -> 6
l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

s = Solution()
merged = s.merge_linked(l1, l2)
s.print_list(merged)
                