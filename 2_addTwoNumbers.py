class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self,l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1 is None and l2 is None:
            return None
        iter1 = l1
        iter2 = l2
        carry_bit = 0
        sum_head = ListNode(0)
        sum_iter = sum_head
        while iter1 and iter2:
            temp = iter1.val + iter2.val + carry_bit
            if temp >= 10:
                carry_bit = 1
                sum_iter.next = ListNode(temp%10)
            else:
                sum_iter.next = ListNode(temp)
                carry_bit = 0
            sum_iter = sum_iter.next
            iter1 = iter1.next
            iter2 = iter2.next
        while iter1:
            temp = iter1.val + carry_bit
            if temp >= 10:
                carry_bit = 1
                sum_iter.next = ListNode(temp%10)
            else:
                sum_iter.next = ListNode(temp)
                carry_bit = 0
            sum_iter = sum_iter.next
            iter1 = iter1.next
        while iter2:
            temp = iter2.val + carry_bit
            if temp >= 10:
                carry_bit = 1
                sum_iter.next = ListNode(temp%10)
            else:
                sum_iter.next = ListNode(temp)
                carry_bit = 0
            sum_iter = sum_iter.next
            iter2 = iter2.next
        if carry_bit == 1:
            sum_iter.next = ListNode(1)
        return sum_head.next
"""
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
"""
"""
l1 = ListNode(0)
l2 = ListNode(0)
"""
l1 = ListNode(9)
l1_iter = l1
for i in range(6):
    l1_iter.next = ListNode(9)
    l1_iter = l1_iter.next
c = l1
print(l1)
while c:
    print(c.val)
    c = c.next
print("l1")
l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
l2.next.next.next = ListNode(9)
atn = Solution()
rel = atn.addTwoNumbers(l1,l2)
while rel:
    print(rel.val)
    rel = rel.next