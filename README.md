# Activity 5: Stacks and Queues

## Description
This Python program demonstrates stacks and queues using both arrays and linked lists. It includes a menu-driven test driver, error handling, a balanced-parentheses checker, and a print-queue simulation.

## Files
- `node.py` - Node class shared by the linked-list implementations.
- `array_stack.py` - Fixed-size array stack with push, pop, peek, is_empty, and is_full.
- `linked_stack.py` - Linked-list stack with push, pop, peek, and is_empty.
- `array_queue.py` - Circular array queue with enqueue, dequeue, peek_front, is_empty, and is_full.
- `linked_queue.py` - Linked-list queue with enqueue, dequeue, peek_front, and is_empty.
- `main.py` - Menu-driven test driver and application exercises.
- `analysis.md` - Written answer to the analysis question.

## Requirements
Python 3. No external libraries are required.

## How to Run
1. Place all Python files in the same folder.
2. Open a terminal or command prompt in that folder.
3. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## How to Test
- Choose **1** or **2** to test the array stack or linked-list stack.
- Choose **3** or **4** to test the circular array queue or linked-list queue.
- Try `pop` or `dequeue` while the structure is empty to see underflow handling.
- Fill an array-based structure and try adding another item to see overflow handling.
- For the circular queue, enqueue items, dequeue one or more, then enqueue again to demonstrate wrap-around.
- Choose **5** to test balanced parentheses such as `([{}])` or `([)]`.
- Choose **6** to simulate print jobs in FIFO order.

## Notes
The array-based stack and queue have fixed capacities. The linked-list versions grow as needed, subject to available memory. The program displays the current structure after each stack or queue operation.
