
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
        print(f"Pushed {element} into the stack.")

    def pop(self):
        if not self.is_empty():
            popped_element = self.stack.pop()
            print(f"Popped {popped_element} from the stack.")
            return popped_element
        else:
            print("Stack is empty. Cannot pop element.")
            return None

    def update(self, new_element):
        if not self.is_empty():
            self.stack[-1] = new_element
            print(f"Updated top element to {new_element}.")
        else:
            print("Stack is empty. Cannot update element.")

    def display(self):
        if not self.is_empty():
            print("Stack elements (Top to Bottom):")
            for element in reversed(self.stack):
                print(element)
        else:
            print("Stack is empty.")

    def is_empty(self):
        return len(self.stack) == 0


def perform_stack_operations(stack):

    while True:
        print("\nChoose an operation:")
        print("1. Push")
        print("2. Pop")
        print("3. Update")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':

            count = int(input("How many elements do you want to push? "))

            for i in range(count):
                element = input(f"Enter element {i+1}: ")
                stack.push(element)

        elif choice == '2':
            stack.pop()

        elif choice == '3':
            element = input("Enter new element to update: ")
            stack.update(element)

        elif choice == '4':
            stack.display()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


# Create a stack object
my_stack = Stack()

# Perform stack operations
perform_stack_operations(my_stack)
