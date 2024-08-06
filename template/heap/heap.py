class MinHeap:
    def __init__(self) -> None:
        self.heap = list()

    def insert(self, key):
        self.heap.append(key)
        self._up_heap(len(self.heap) - 1)

    def _up_heap(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self.heap[idx] < self.heap[parent_idx]:
            self.heap[idx], self.heap[parent_idx] = (
                self.heap[parent_idx],
                self.heap[idx],
            )
            self._up_heap(parent_idx)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._down_heap(0)

        return root

    def _down_heap(self, idx):
        smallest = idx
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[smallest]
        ):
            smallest = right_child

        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._down_heap(smallest)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def __str__(self):
        return str(self.heap)


def main():
    min_heap = MinHeap()
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(1)
    print("heap:", min_heap)

    print("smallest vaule:", min_heap.extract_min())
    print("heap:", min_heap)

    print("smallest vaule:", min_heap.extract_min())
    print("heap:", min_heap)

    min_heap.insert(5)
    min_heap.insert(4)
    print("heap:", min_heap)


if __name__ == "__main__":
    main()
