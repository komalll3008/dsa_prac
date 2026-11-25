
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert element
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue")

    # Delete element
    def dequeue(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print(temp.data, "deleted from queue")

        self.front = self.front.next

        if self.front is None:
            self.rear = None

    # Display queue
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print("Queue elements:")

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Peek front element
    def peek(self):
        if self.front is None:
            print("Queue is Empty")
        else:
            print("Front element:", self.front.data)


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.display()

q.peek()
