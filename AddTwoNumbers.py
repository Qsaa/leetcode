from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    number_transition = 0
    previous = None
    first = None
    while l1 or l2:
        if l1 is None:
            summary = l2.val + number_transition
            l2 = l2.next
        elif l2 is None:
            summary = l1.val + number_transition
            l1 = l1.next
        else:
            summary = l1.val + l2.val + number_transition
            l1 = l1.next
            l2 = l2.next

        number_transition = summary // 10
        now = ListNode(summary % 10, None)
        if previous is not None:
            previous.next = now
        else:
            first = now
        previous = now

    if number_transition != 0:
        now = ListNode(number_transition, None)
        previous.next = now
    return first


def printList(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


def createList(n_list: list) -> ListNode:
    first = ListNode(n_list[0], None)
    previous = first
    for i in range(1, len(n_list)):
        now = ListNode(n_list[i], None)
        previous.next = now
        previous = now
    return first


l1 = createList([9, 9, 9, 9, 9, 9, 9])

l2 = createList([9, 9, 9, 9])

printList(addTwoNumbers(l1, l2))
