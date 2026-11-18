class node:
    def __init__(self, pid, name, pr):
        self.pid = pid
        self.name = name
        self.priority = pr
        self.next = None


class priorityqueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if new_node.priority < 1 or new_node.priority > 4:
            print("Invalid Priority!")
            return

        if self.front == None:
            self.front = new_node
            return

        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

        print("Process added successfully!")

    def dequeue(self):
        if self.front:
            temp = self.front
            print("Executed Process:", temp.name)
            self.front = self.front.next
            temp = None
        else:
            print("Queue is empty!")

    
    def display_next(self):
        if self.front:
            print("Next Process:")
            print("ID:", self.front.pid)
            print("Name:", self.front.name)
            print("Priority:", self.front.priority)
        else:
            print("Queue is empty!")

    def display(self):
        if self.front == None:
            print("Queue is empty!")
            return

        temp = self.front

        while temp:
            print("ID:", temp.pid,
                  "Name:", temp.name,
                  "Priority:", temp.priority)
            temp = temp.next

    # 5. Count Processes
    def count(self):
        temp = self.front
        c = 0

        while temp:
            c += 1
            temp = temp.next

        print("Total Pending Processes:", c)


pq = priorityqueue()

pq.enqueue(node(101, "System", 1))
pq.enqueue(node(102, "Browser", 2))
pq.enqueue(node(103, "Background", 3))
pq.enqueue(node(104, "Interactive", 2))
pq.enqueue(node(105, "Low", 4))

print("\nAll Processes:")
pq.display()

print("\nNext Process:")
pq.display_next()

print("\nExecute Process:")
pq.dequeue()

print("\nRemaining Processes:")
pq.display()

print("\nCount Processes:")
pq.count()