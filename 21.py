class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(30)

position = 2
value = 20

new_node = Node(value)
temp = head

for i in range(position - 2):
    temp = temp.next

new_node.next = temp.next
temp.next = new_node

while head:
    print(head.data, end=" -> ")
    head = head.next