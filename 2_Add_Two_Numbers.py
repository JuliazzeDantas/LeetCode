#Accepted: 58ms 17.52MB
'''You are given two non-empty linked lists representing two non-negative integers. The digits
 are stored in reverse order, and each of their nodes contains a single digit. Add the two 
 numbers and return the sum as a linked list.You may assume the two numbers do not contain any 
 leading zero, except the number 0 itself.'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        n1 = 0
        n2 = 0
        result = []
        count = 0

        while (l1 is not None) or (l2 is not None):
            if (l1 is not None):
                n1 = n1 + (l1.val*pow(10, count))
                l1 = l1.next
            if (l2 is not None):
                n2 = n2 + (l2.val*pow(10, count))
                l2 = l2.next
            count = count + 1
        
        aux = n1 + n2
        aux = str(aux)
        print(n1)
        print(n2)
        print(aux)
        point = None
        for char in aux:
            result = ListNode(int(char), point)
            point = result
        return result
        