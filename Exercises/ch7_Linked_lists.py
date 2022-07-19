"""
Created on Fri Jun  3 10:32:55 2022

@author: seyma
"""

# R-7.5 Implement a function that counts the number of nodes in a circularly
# linked list
def count_nodes(c_l):
    pass
    # count=0
    # starting_node=c_l.
    #len function varmış niye tek tek sayayım ki 
    #ama olmasaydı referenace node ile başlayıp tekrar aynı node a gelene kadar sayardık


# C-7.39 To better model a FIFO queue in which entries may be deleted before
# reaching the front, design a PositionalQueue class that supports the complete queue ADT, yet with enqueue returning a position instance and support for a new method, delete(p), that removes the element associated
# with position p from the queue. You may use the adapter design pattern
# (Section 6.1.2), using a PositionalList as your storage.    
 
class DivError(Exception):
    pass

class LinkedList:
   
    def __init__(self):
        self.head = None  # Reference to head node
        self.size = 0  # Size of Linked List


    class Node:
        def __init__(self, element, nextt):
            self.data = element
            self.next = nextt

    def insert_last(self, e):
        e=self.Node(e,None)
        if self.size==0:
            self.head=e
        else:
            tail=self.find_tail()
            tail.next=e
        self.size+=1
    
    def insert_first(self,e):
        self.head=self.Node(e,self.head)    
        self.size+=1

    def find_tail(self):
        current=self.head
        while current.next!=None:
            current=current.next
        tail=current
        return tail

    def print_contents(self):
        format_str = "%s" #if self.taskNo == 1 else "%d"
        if self.size == 0:
            print(" ")
            return
        current = self.head
        while (current.next != None):
            print((format_str + " -> ") % current.data, end="")
            current = current.next

        print(format_str % current.data)
        
class FIFO_queue(LinkedList):
    
    # def __init__(self):
        # self.head = None  # Reference to head node
        # self.size = 0  # Size of Linked List
##use insert last
# delete first normallly
#delete a spesific node for ...
    def del_first_in(self):
        ##del tail
        first=self.head.data
        self.head=self.head.next
        return first
    def del_node(self,e):
        current=self.head
        while current.next.data!=e:
            current=current.next
        prev=current
        c=prev.next
        next_node=c.next
        prev.next=next_node
        return c.data
        
# F=FIFO_queue()
# F.insert_last(2)
# F.insert_last(3)
# F.insert_last(4)
# F.insert_last(5)
# F.insert_last(6)
# print(F.del_first_in())
# print(F.del_node(5))
# F.print_contents()

 
# P-7.44 Write a simple text editor that stores and displays a string of characters
# using the positional list ADT, together with a cursor object that highlights
# a position in this string. A simple interface is to print the string and then
# to use a second line of output to underline the position of the cursor. Your
# editor should support the following operations:
# • left: Move cursor left one character (do nothing if at beginning).
# • right: Move cursor right one character (do nothing if at end).
# • insert c: Insert the character c just after the cursor.
# • delete: Delete the character just after the cursor (do nothing at end).


    
class DoublyLinkedBase:
    
    class Node:
        def __init__(self, element, prev, next):
            self.data = element
            self.prev= prev
            self.next = next


    def __init__ (self):

        self.header = self.Node(None, None, None)
        self.trailer = self.Node(None, None, None)
        self.header. next = self.trailer # trailer is after header
        self.trailer. prev = self.header # header is before trailer
        self.size = 0 # number of elements

    def __len__ (self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_between(self, e, predecessor, successor):

        newest = self. Node(e, predecessor, successor) # linked to neighbors
        predecessor. next = newest
        successor. prev = newest
        self. size += 1
        return newest

    def delete_node(self, node):

        predecessor = node.prev
        successor = node.next
        predecessor. next = successor
        successor. prev = predecessor
        self. size -= 1
        element = node. element # record deleted element
        node. prev = node. next = node. element = None # deprecate node
        return element
    
    def print_contents(self):
        format_str = "%s" 

        current = self.header
        while (current.next != None):
            print((format_str + " <-> ") % current.data, end="")
            current = current.next

        print(format_str % current.data)
            
class TextEditor(DoublyLinkedBase):
       
    
    def add_text(self,text):
        if len(text)==1:
            self.header.data=text[0]
            self.trailer=self.header
            self.header.next=None
            self.trailer.prev=None
            
        else:
            self.header.data=text[0]
            current=self.header
            for i in range(len(text)-1):
                new_node=self.Node(text[i+1],None,None)
                current.next=new_node
                old_current=current
                current=new_node
                current.prev=old_current
                self.size+=len(text)
            self.trailer=current
            self.trailer.prev=current.prev
            
    def find_cursor(self):
        current=self.header
        while current.data!="|":
            current=current.next
        return current
            
    def right(self):
        cursor=self.find_cursor()
        if cursor==self.trailer:
            pass
        elif cursor.next!=None:
            if cursor.prev==None and cursor.next.next==None:
                cursor.prev=cursor.next
                cursor.next.next=cursor
                self.header=cursor.prev
                self.header.prev=None
                self.trailer=cursor
                cursor.next=None                
                
            elif cursor.prev==None:
                self.header=cursor.next
                self.header.prev=None
                cursor.next=cursor.next.next  
                cursor.next.prev=None
                self.header.next=cursor
                cursor.next.prev=cursor
                cursor.prev=self.header
            
            elif cursor.next.next==None:
                cursor.prev.next=cursor.next
                cursor.next.prev=cursor.prev
                cursor.next.next=cursor
                cursor.prev=cursor.next
                self.tailer=cursor
                cursor.next=None
                
                
            else:    
                cursor.prev.next=cursor.next
                cursor.next=cursor.next.next
                cursor.next.prev=cursor
                cursor.prev.next.next=cursor
                cursor.prev.next.prev=cursor.prev              
                cursor.prev=cursor.prev.next

    def left(self):
        cursor=self.find_cursor()
        if cursor==self.header:
            pass
        elif cursor.prev!=None:
            if cursor.next==None and cursor.prev.prev==None:
                cursor.next=cursor.prev
                cursor.prev.prev=cursor
                self.trailer=cursor.next
                self.trailer.next=None
                self.header=cursor
                cursor.prev=None                
                
            elif cursor.next==None:
                self.trailer=cursor.prev
                self.trailer.next=None
                cursor.prev=cursor.prev.prev  
                cursor.prev.next=None
                self.trailer.prev=cursor
                cursor.prev.next=cursor
                cursor.next=self.trailer
            
            elif cursor.prev.prev==None:
                cursor.next.prev=cursor.prev
                cursor.prev.next=cursor.next
                cursor.prev.prev=cursor
                cursor.next=cursor.prev
                self.header=cursor
                cursor.prev=None
                
            else:    
                cursor.next.prev=cursor.prev
                cursor.prev=cursor.prev.prev
                cursor.prev.next=cursor
                cursor.next.prev.prev=cursor
                cursor.next.prev.next=cursor.next              
                cursor.next=cursor.next.prev
                
    def insert(self,character):
        cursor=self.find_cursor()
        if cursor==self.trailer:
            ch_node=self.Node(character,cursor,None)
            cursor.next=ch_node
            self.trailer=ch_node
        else:
            ch_node=self.Node(character,cursor,cursor.next)
            cursor.next.prev=ch_node
            cursor.next=ch_node
            
    def delete(self):
        cursor=self.find_cursor()
        if cursor==self.trailer:
            pass
        elif cursor.next.next==None:
            self.trailer=cursor
            self.trailer.next=None
        else:
            cursor.next=cursor.next.next
            cursor.next.prev=cursor
        
                
                

        
T=TextEditor()
T.add_text("|dd")
T.right()
# T.left()
T.delete()
T.insert("k")
T.print_contents()


















