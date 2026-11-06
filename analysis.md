# Analysis Question

The linked-list stack pushes at the head because the head can be updated directly, so the operation takes **O(1)** time. If we push or remove items at the tail of a singly linked list, we may need to travel through the list, which takes **O(n)** time. The array queue must be circular so that empty spaces at the beginning of the array can be used again after dequeue operations. Using modulo (`%`) allows the front and rear positions to return to index 0 after reaching the end of the array, while keeping enqueue and dequeue at **O(1)** time.
