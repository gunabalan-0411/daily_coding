class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.q = [None] * k
        self.size = 0
        self.head = 0
        self.tail = k - 1

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.head = (self.head - 1 + self.k) % self.k
        self.q[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.tail = (self.tail + 1) % self.k
        self.q[self.tail] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.tail = (self.tail - 1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.tail]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
