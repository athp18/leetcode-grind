# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        return self.val < other.val
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        class Compare:
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val

        # Initialize the min heap
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, Compare(l)))

        dummy = ListNode(0)
        curr = dummy

        # Main loop
        while heap:
            val, i, wrapper = heapq.heappop(heap)
            curr.next = wrapper.node
            curr = curr.next

            if curr.next:
                heapq.heappush(heap, (curr.next.val, i, Compare(curr.next)))

        return dummy.next
