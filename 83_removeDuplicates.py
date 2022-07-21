class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

class Solution:
    def removeDuplicates(self, head):
        help_node = ListNode(0)
        current_help = help_node
        current = head
        while current:
            if current.next is None:
                current_help.next = current
                break
            elif current.next.val == current.val:
                current = current.next
            elif current.next.val != current.val:
                current_help.next = current
                current_help = current_help.next
                current = current.next
        return help_node.next

head = ListNode(1)
h1 = ListNode(2)
h2 = ListNode(2)
h3 = ListNode(2)
h4 = ListNode(3)
h5 = ListNode(3)
h6 = ListNode(3)
head.next = h1
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6


rd = Solution()
rel = rd.removeDuplicates(head)
#"""
while rel:
    print(rel.val)
    rel = rel.next