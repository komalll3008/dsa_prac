import heapq

process_queue = []
counter = 0

# 1. Add Process
def enqueue():
    global counter

    pid = int(input("Enter Process ID: "))
    name = input("Enter Process Name: ")
    priority = int(input("Enter Priority (1-4): "))

    if priority < 1 or priority > 4:
        print("Invalid Priority!")
        return

    heapq.heappush(process_queue, (priority, counter, pid, name))
    counter += 1

    print("Process added successfully!")


# 2. Execute Process
def dequeue():
    if len(process_queue) == 0:
        print("No process available!")
    else:
        p = heapq.heappop(process_queue)
        print("Executed Process:", p[3])


# 3. View Next Process
def display_next():
    if len(process_queue) == 0:
        print("No process available!")
    else:
        p = process_queue[0]
        print("Next Process:")
        print("Process ID:", p[2])
        print("Process Name:", p[3])
        print("Priority:", p[0])


# 4. Display All Processes
def display_all():
    if len(process_queue) == 0:
        print("No pending processes!")
    else:
        print("\nPending Processes:")
        print("ID\tName\tPriority")

        for p in sorted(process_queue):
            print(p[2], "\t", p[3], "\t", p[0])


# 5. Count Processes
def count():
    print("Total Pending Processes:", len(process_queue))


# Main Menu
while True:
    print("\n--- CPU PROCESS SCHEDULING ---")
    print("1. Add Process")
    print("2. Execute Process")
    print("3. View Next Process")
    print("4. Display All Processes")
    print("5. Count Processes")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display_next()

    elif choice == 4:
        display_all()

    elif choice == 5:
        count()

    elif choice == 6:
        print("Program Terminated!")
        break

    else:
        print("Invalid Choice!")