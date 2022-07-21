
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        head = newlist = ListNode(0)
        while (list1 and list2):
            if list1.val < list2.val:
                newlist.next = list1
                list1 = list1.next
            else:
                newlist.next = list2
                list2 = list2.next
            newlist = newlist.next
        newlist.next = list1 or list2
        return head.next
list1 =ListNode(1)
d1 = ListNode(2)
d2 = ListNode(4)
list1.next = d1
d1.next = d2

list2 = ListNode(1)
e1 = ListNode(2)
e2 = ListNode(3)
list2.next = e1
e1.next = e2


out = Solution()
rel = out.mergeTwoLists(list1, list2)
while rel != None:
    print("rel.val = ", rel.val)
    rel = rel.next



"""
#===================  This verson works. But it is not efficient. ===================#
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        else:
            temp1 = list1
            temp2 = list2
            outlist = None
            if temp1.val <= temp2.val:  # list1's first node is smaller
                outlist = list1
            else:
                outlist = list2

            if outlist == list1:  # insert nodes on list1
                while temp2 is not None:
                    if temp1.val <= temp2.val and temp1.next is None:
                        print("================case1====================")
                        temp1.next = temp2
                        break
                    elif temp1.val <= temp2.val and temp1.next.val <= temp2.val:
                        print("================case2====================")
                        # temp1 pointer moves to the next node
                        temp1 = temp1.next
                    elif temp1.val <= temp2.val and temp1.next.val > temp2.val:
                        print("================case3====================")
                        # insert
                        temp1.next = ListNode(temp2.val, temp1.next)
                        temp1 = temp1.next
                        temp2 = temp2.next
            if outlist == list2: # insert nodes to list2
                while temp1 is not None:
                    if temp2.val <= temp1.val and temp2.next is None:
                        print("================case1====================")
                        temp2.next = temp1
                        break
                    elif temp2.val <= temp1.val and temp2.next.val <= temp1.val:
                        print("================case2====================")
                        temp2 = temp2.next
                    elif temp2.val <= temp1.val and temp2.next.val > temp1.val:
                        print("================case3====================")
                        temp2.next = ListNode(temp1.val, temp2.next)
                        temp2 = temp2.next
                        temp1 = temp1.next
            return outlist



"""