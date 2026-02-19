#Zadanie 13
class NoneTypeError(Exception):
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
            current = self.head
        else:
            curr_item = self.head
            while True:
                if curr_item.next is None:
                    curr_item.next = new_element
                    current = curr_item.next
                    break
                curr_item = curr_item.next

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
                break
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
                 break
            curr_item = curr_item.next
        if not is_deleted:
            raise ValueNotFoundError("Brak wartości")

    def display_elements(self):
        if self.head is None:
            data = self.head
        data = self.head.data
        curr_item = self.head
        while curr_item.next is not None:
          curr_item = curr_item.next
          data += curr_item.data
        return data

    def display_elements_2(self): #Metoda join():
        temp_list = list()
        if self.head is None:
            raise EmptyListError("Lista pusta")
        curr_item = self.head
        curr_data = self.head.data
        temp_list.append(curr_data)
        while curr_item.next is not None:
            temp_list.append(curr_item.next.data)
            curr_item = curr_item.next
        x = '-->'.join(temp_list)
        return x

    def reverse_elements(self):
        prev_item = None
        curr_item = self.head
        while curr_item:
            next_item = curr_item.next
            curr_item.next = prev_item
            prev_item = curr_item
            curr_item = next_item
        return prev_item


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
        if self.head is None:
            raise StopIteration
        item_data = self.head.data
        self.head = self.head.next
        return item_data


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
ll.append_value('C')
ll.append_value('D')

x = iter(ll)
print(next(x))
print(next(x))
print(next(x))





















