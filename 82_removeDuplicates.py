class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeDuplicates(self, head):
        count = 0
        help_node = ListNode(0)
        current_help = help_node
        current_head = head
        duplicates = False
        if head is None:
            return None
        while current_head.next:
            if not duplicates and current_head.next.val != current_head.val:
                print("current.val = ", current_head.val)
                current_help.next = current_head
                current_help = current_help.next
                current_head = current_head.next
            elif duplicates and current_head.next.val == current_head.val:
                current_head = current_head.next
            elif duplicates and current_head.next.val != current_head.val:
                current_head = current_head.next
                duplicates = False
            elif current_head.next.val == current_head.val:
                duplicates = True
                current_head = current_head.next
        if not duplicates:
            current_help.next = current_head
        if duplicates:
            current_help.next = None
        return help_node.next

# [1,2,3,3,4,4,5]
head = ListNode(1)
h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(2)
h4 = ListNode(3)
h5 = ListNode(3)
h6 = ListNode(5)
head.next = h1
h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5
h5.next = h6
print("length of linked node = ", len(head))

rd = Solution()
rel = rd.removeDuplicates(head)
#"""
while rel:
    print(rel.val)
    rel = rel.next
#"""