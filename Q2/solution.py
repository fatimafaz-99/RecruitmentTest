 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def display(self):
        printNode = self
        list = []
        while printNode is not None:
            list.append(printNode.val)
            printNode = printNode.next
        print(list)
class Solution:
   def __init__(self):
      self.headval = None
   def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


if __name__ == '__main__':
    list1 = Solution()
    list1.headval = ListNode("1")
    e2 = ListNode("2")
    e3 = ListNode("3")
    e4 = ListNode("4")
    e5 = ListNode("5")
    list1.headval.next=e2
    e2.next=e3
    e3.next=e4
    e4.next=e5
    list1.headval.display()
    list1.removeNthFromEnd(list1.headval,4).display()
        
