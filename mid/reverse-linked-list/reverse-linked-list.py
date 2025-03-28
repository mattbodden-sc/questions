from datetime import datetime


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node
    
    def read(self, index):
        current_node = self.first_node
        current_index = 0
        while current_index < index:
            current_node = current_node.next_node
            current_index += 1
            if current_node is None:
                return None
        return current_node.data
    
    def index_of(self, value):
        current_node = self.first_node
        current_index = 0
        while current_node is not None:
            if current_node.data == value:
                return current_index
            current_node = current_node.next_node
            current_index += 1
        return None
    
    def insert_at_index(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next_node = self.first_node
            self.first_node = new_node
            return
        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
    
    def delete_at_index(self, index):
        if index == 0:
            self.first_node = self.first_node.next_node
            return
        current_node = self.first_node
        current_index = 0
        while current_index < index - 1:
            current_node = current_node.next_node
            current_index += 1
        current_node.next_node = current_node.next_node.next_node

    def reverse(self):
        pass


if __name__ == "__main__":
    # Read values from the file
    with open('../reverse-linked-list-input.txt', 'r') as file:
        values = [line.strip() for line in file.readlines()]

    # Create nodes from the values
    if not values:
        print("The input file is empty.")
    else:
        first_node = Node(values[0])
        current_node = first_node
        for value in values[1:]:
            new_node = Node(value)
            current_node.next_node = new_node
            current_node = new_node

        # Create the linked list
        linked_list = LinkedList(first_node)

        # Example usage
        print("Linked list created. First node value:", linked_list.read(0))
        # Print the linked list
        current_node = linked_list.first_node
        print("Linked list values:")
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")
        # Reverse the linked list - uncomment the following lines to test.
        # linked_list.reverse()
        # Print the reversed linked list
        # current_node = linked_list.first_node
        # print("Reversed linked list values:")
        # while current_node:
        #     print(current_node.data, end=" -> ")
        #     current_node = current_node.next_node
        # print("None")
