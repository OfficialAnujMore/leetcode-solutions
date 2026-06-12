"""
Short Intuition:
This implements a Stack using a single Queue.
The clever part is in pop(): to get the last element (stack behavior) from a queue (which normally gives you the first), you rotate everything backward. Move the first n-1 elements to the back, which pushes the last element to the front. Then pop it.

Example: [1, 2, 3] → rotate → [2, 3, 1] → [3, 1, 2] → pop 3
Key insight: LIFO from FIFO by strategic rotation.
"""

from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:

        current_length = len(self.q)

        for _ in range(current_length - 1):
            ele = self.q.popleft()
            self.q.append(ele)
        return self.q.popleft()

    def top(self) -> int:
        if len(self.q) == 0:
            return -1
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
