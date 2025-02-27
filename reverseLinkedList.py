'''Given the head of a singly linked list, reverse the list, and return the reversed list.
head = [1,2,3,4,5]
out: [5,4,3,2,1]
'''

class LinkedNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next


def buildLinkedList(arr) -> LinkedNode:
   head = LinkedNode(arr[0]) # 1
   previous = head
   for idx in range(1, len(arr)):
       el = LinkedNode(arr[idx])
       previous.next = el
       previous = el
   return head

def printLinkedList(ln: LinkedNode) -> None:
   while ln is not None:
       print(ln.val)
       ln = ln.next

def reverseLinkedNode(head: LinkedNode) -> LinkedNode:
   if head is None or head.next is None:
       return head
   reversed_head = reverseLinkedNode(head.next)
   head.next.next = head
   head.next = None
   return reversed_head


head = [1,2,3,4,5]
linked_head = buildLinkedList(head)
reversed_head = reverseLinkedNode(linked_head)
printLinkedList(reversed_head)
# printLinkedList(buildLinkedList(head))
