'''
Quest:
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

    Example:
    Input:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    Output: 1->1->2->3->4->4->5->6

Solution:
    - use priority queue in Queue library, it can help sort node based on a priority number
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        q = PriorityQueue()
        root = ListNode(None)
        curr = root

        for node in lists:
            if node:
                q.put((node.val, id(node), node))

        while q.qsize() > 0:
            curr.next = q.get()[2]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val, id(curr.next), curr.next))

        return root.next
