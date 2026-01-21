#Zadanie 13

from logging import raiseExceptions
class NoneType(Exception):
    """Exception for NoneType"""

class EmptyListError(Exception):
    """Exception for empty List"""

class ValueNotFoundError(Exception):
    """Exception for not found value"""

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append_value(self, data):
        new_element = Node(data)
        if self.head is None:
            self.head = new_element
            data = self.head
        else:
            curr_item = self.head
            while True:
                if curr_item.next is None:
                    curr_item.next = new_element
                    data = curr_item.next
                    break
                curr_item = curr_item.next
        return data.data


    def find_value(self, value):
        is_found = False
        found_value = ""
        if self.head is None:
            raise EmptyListError("Lista jest pusta")
        if self.head.data == value:
            found_value = self.head.data
            is_found = True
        curr_item = self.head
        while curr_item is not None:
            if curr_item and curr_item.data == value:
                found_value = curr_item
                is_found = True
            curr_item = curr_item.next
        if is_found:
            return found_value

    def delete_value(self, value):
        is_deleted = False
        if self.head is None:
            raise EmptyListError("Lista jest pusta")
        if self.head.data == value:
            self.head = self.head.next
            is_deleted = True
        curr_item = self.head
        while curr_item is not None:
            if curr_item.next and curr_item.next.data == value:
                 curr_item.next = curr_item.next.next
                 is_deleted = True
            curr_item = curr_item.next
        if not is_deleted:
            raise ValueNotFoundError("Brak wartości")

    def display_elements(self):
        if self.head is None:
            return "Pusta lista"
        first_item_data = self.head.data
        curr_item = self.head
        while curr_item.next is not None:
          curr_item = curr_item.next
          first_item_data+=f"{curr_item.data}"
        return first_item_data

    def reverese_elements(self ):
        reverse_list = ll.display_elements()[::-1]
        return reverse_list

    def __len__(self):
        amount = 0
        curr_item = self.head
        while curr_item is not None:
            amount+=1
            curr_item = curr_item.next
        return amount

    def __iter__(self):
        return self

    def __next__(self):
       curr_item = self.head
       if curr_item is None:
           raise StopIteration
       self.head = self.head.next
       return curr_item.data

    def __str__(self):
        curr_item = self.head
        to_be_printed = curr_item.data
        while curr_item.next is not None:
             curr_item = curr_item.next
             to_be_printed+=f"-->{curr_item.data}"
        return to_be_printed



ll = LinkedList()
ll.append_value('A')
ll.append_value('B')
ll.__iter__()
print(ll.__next__())
print(ll.__next__())
print(ll.__next__())
print(ll.__next__())













