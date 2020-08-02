"""
listnode module: has class ListNode and class SingleLinkedList. Do not make any changes.
"""


from cells import Cell

class ListNode:
    def __init__(self, data):
        """ Constructor to initiate a node in a singly-liked list """
        self.data = data
        self.next = None

    def __repr__(self):
        pass
        
    def has_value(self, value):
        """ Method compares the value with the node data and returns True or False """

        if self.data == value:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)

class SingleLinkedList:
    node_ptr = ListNode("")
    
    def __init__(self):
        """ Method to initialize the single linked list object"""
        self.head = None
        
    def destroy(self):
        self.head = None

    def __del__(self):
        print("Object destroyed")

    def get_next_node(self, item):
        return item.next

    def get_node(self):
        return node_ptr
    
    def append_node(self, item):
        """ append_node(self, item): appends linknode to link list
        """
        node_ptr = ListNode("")

        if isinstance(item, ListNode):
            new_node = item
        else:
            new_node = ListNode(item)
            new_node.next = None
            
        if self.head is None:
            """ Second, if there are no nodes in the list, make new_node the first node."""

            self.head = new_node
        else:
            """Otherwise, insert new_node at end. """
            node_ptr = self.head

            """ Traverse the linked list using the node_ptr, and find the last node."""
            while(node_ptr.next):
                node_ptr = node_ptr.next

            """Insert new_node as the last node. """
            node_ptr.next = new_node

    def search_list(self, value):
        node_ptr = self.head
        current_node = self.head

        if isinstance(value, str):
            while current_node is not None:
                if current_node.data.header == value:
                    return current_node.data
                else:
                    current_node = current_node.next
        elif isinstance(value, dict):
            while current_node is not None:
                if current_node.data == value:
                    return current_node
                else:
                    current_node = current_node.next
        return None

    def traverse_list(self, index, length):
        """Do not change"""
        while index < length:
            if index == 0:
                global node_ptr
                node_ptr = self.head
                return node_ptr.data
            else:
                node_ptr = node_ptr.next
                return node_ptr.data
            
        
    def list_length(self):
        """ Method returns the number of list items. """
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next

        return count

    def output_list(self):
        """ Method outputs the value of the nodes in the list """
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

        return

    def unordered_search(self, value):
        """ Method searches the linked list for the node that has passed value as parameter """
        node_ptr = ListNode("")
        node_ptr = self.head

        current_node = self.head
        node_id = 1

        results = []

        while current_node.next is not None:
            if current_node.has_value(value):
                node_ptr = current_node
                break
            else:
                current_node = current_node.next
                
        return node_ptr

    def has_node(self, value):
        current_node = self.head
        if isinstance(value, dict):
            while current_node is not None:
                if current_node.data == value:
                    print(value)
                    return True
                else:
                    current_node = current_node.next
        return False
        
        
