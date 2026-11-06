from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_stack_menu(stack):
    while True:
        print("\\n1. Push  2. Pop  3. Peek  4. Is empty?  5. Is full?  0. Back")
        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to push: ")
                stack.push(value)
                print("Value pushed.")
            elif choice == "2":
                print("Removed:", stack.pop())
            elif choice == "3":
                print("Top value:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                if hasattr(stack, "is_full"):
                    print("Is full:", stack.is_full())
                else:
                    print("Linked stack has no fixed capacity.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        print("Current stack:", stack)


def show_queue_menu(queue):
    while True:
        print("\\n1. Enqueue  2. Dequeue  3. Peek front  4. Is empty?  5. Is full?  0. Back")
        choice = input("Choose an operation: ")

        try:
            if choice == "1":
                value = input("Enter value to enqueue: ")
                queue.enqueue(value)
                print("Value added.")
            elif choice == "2":
                print("Removed:", queue.dequeue())
            elif choice == "3":
                print("Front value:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                if hasattr(queue, "is_full"):
                    print("Is full:", queue.is_full())
                else:
                    print("Linked queue has no fixed capacity.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)

        print("Current queue:", queue)


def balanced_parentheses(expression):
    """Return True when (), [] and {} are correctly matched."""
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for character in expression:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != matching[character]:
                return False

    return len(stack) == 0


def print_queue_simulation():
    """Demonstrate FIFO printing using the linked queue."""
    queue = LinkedQueue()
    print("\\nEnter print jobs. Leave the job ID blank to stop.")
    while True:
        job_id = input("Job ID: ")
        if job_id == "":
            break
        pages = input("Number of pages: ")
        try:
            pages = int(pages)
            if pages <= 0:
                print("Pages must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid number of pages.")
            continue
        queue.enqueue({"id": job_id, "pages": pages})
        print("Job added. Current waiting list:", queue)

    print("\\nPrinting jobs in FIFO order:")
    position = 1
    while not queue.is_empty():
        job = queue.dequeue()
        print(f"{position}. Job {job['id']} - {job['pages']} page(s)")
        position += 1
    if position == 1:
        print("There were no jobs to print.")


def main():
    while True:
        print("\\n========== STACKS AND QUEUES ==========")
        print("1. Array Stack")
        print("2. Linked List Stack")
        print("3. Circular Array Queue")
        print("4. Linked List Queue")
        print("5. Check Balanced Parentheses")
        print("6. Simulate Print Queue")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            capacity = int(input("Enter stack capacity: "))
            show_stack_menu(ArrayStack(capacity))
        elif choice == "2":
            show_stack_menu(LinkedStack())
        elif choice == "3":
            capacity = int(input("Enter queue capacity: "))
            show_queue_menu(ArrayQueue(capacity))
        elif choice == "4":
            show_queue_menu(LinkedQueue())
        elif choice == "5":
            expression = input("Enter an expression: ")
            if balanced_parentheses(expression):
                print("The parentheses are balanced.")
            else:
                print("The parentheses are not balanced.")
        elif choice == "6":
            print_queue_simulation()
        elif choice == "0":
            print("Program ended.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
