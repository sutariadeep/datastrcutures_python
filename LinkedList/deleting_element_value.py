# Python program to delete a node in a linked list
# with a given value

# Node class 
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    # Constructor to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Given a reference to the head of a list 
    # and a value, delete the node with that value
    def deleteNode(self, value):

        # If linked list is empty
        if self.head == None:
            return


        # If head needs to be removed
        while self.head != None and self.head.data == value:
            temp = self.head
            self.head = self.head.next
            temp = None
        
        #current points to the next link while temp points
        #to the node to be removed while scanning through
        #the list
        current = self.head
        while current.next != None:
            if current.next.data == value:
                temp = current.next
                current.next = temp.next
                temp = None
            else:
                current = current.next    


    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print " %d " %(temp.data),
            temp = temp.next


# Driver program to test above function
llist = LinkedList()
llist.push(7)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(8)

value = 7
print "Created Linked List: "
llist.printList()
llist.deleteNode(value)
print
print "After deletion of element valued %s:"%(value)
llist.printList()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
