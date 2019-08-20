class _ListElement:
    '''Class for keeping track of elements in the list.'''
    def __init__(self,initialValue):
        self.element = initialValue
        self.next = None

class LinkedList:
    '''A linked list class'''

    def __init__(self):
        '''Construct an empty list'''
        self._first = None #Private attribute of first listobject
        self._last = None #Private attribute of last listobject
        self._size = 0 #Private attribute of the list size

    def addFirst(self,value):
        '''Adds an element to the beginning of the list'''
        obj = _ListElement(value)#Creates an object of the _ListElement() class
        obj.next = self._first #Sets the object at the first position in the list
        self._first = obj #Sets the new first object
        if self._size == 0: #Incase the list was empty it sets the new last object
            self._last = obj
        self._size += 1

    def addLast(self,value):
        '''Adds an item to the end of the list'''
        obj = _ListElement(value)#Creates an object of the _ListElement() class
        temp=self._last
        self._last = obj #Sets the next to last object pointing on the new last obj
        if not temp==None:
            temp.next = obj
        if self._size == 0:
            self._first=obj
        self._last = obj #A new last object
        self._size+=1

    def getFirst(self):
        '''Returns the first element in the list'''
        if self._first == None:
            return None
        else:
            return self._first.element

    def getLast(self):
        '''Returns the last element of the list'''
        if self._last == None:
            return None
        else:
            return self._last.element

    def getIndex(self,index):
        '''Returns the item on the index position'''
        if index > self._size or index<=0: #If index exceeds the lists size (first obj has index 1)
            return None
        else:
            item=self._first
            for i in range(index-1):
                item = item.next
            return item.element

    def removeFirst(self):
        '''Removes the first item from the list and returns it'''
        if self._first==None:
            return None
        else:
            first = self._first
            second= self._first.next
            self._first = second
            self._size -= 1
            return first.element


    def clear(self):
        '''Clears the list of elements'''
        self._first = None
        self._last = None
        self._size=0

    def size(self):
        '''Returns the number of elements in the list'''
        if self._size==0:
            return None
        else:
            return self._size

    def string(self):
        string= "["
        element = self._first
        if element != None:
            string += " " + str(element.element)
        for i in range(self._size-1):
            element = element.next
            string += ", " + str(element.element)

        string +=  "]"
        return string

    def _healthy(self):
        '''Asserts certain rules the class SHOULD fulfill'''
        counter=0
        first= self._first
        while first!=None:
            counter +=1
            first=first.next
        assert counter == self._size #Makes sure the amount of elements is equal to the ._size attribute
        if self._size == 0: #If there are no elements in the list there should be no first and last elements
            assert self._first == None
            assert self._last == None
        else: #If there are elements in the list there shoould be both a first and a last element in the list
            assert self._first != None
            assert self._last != None
        if self._size!=0:
            assert self._last.next == None #Asserts the last elements IS the last element


#TESTKOD
l = LinkedList()

l._healthy() #I call this testing-mathod everytime the list is updated.

#Method-testing

assert l.removeFirst() == None
l._healthy()
assert l.getFirst() == None
assert l.getLast() == None
assert l.size() == None
assert l.string() == "[]"

for i  in range(10):# Adds elements to the list: [0,1,2,3,4,5,6,7,8,9]
    l.addLast(i)
    l._healthy() #This operation will take alot of time for larger lists.

assert l.getFirst() == 0
assert l.getLast() == 9
assert l.size() == 10
assert l.string()== "[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"

for i in range(10):
    assert l.getIndex(i+1) == i
    l._healthy()

assert l.removeFirst() == 0
l._healthy()
assert l.getFirst() == 1
assert l.getLast() == 9
assert l.size() == 9
l.clear()
l._healthy()

assert l.removeFirst() == None
l._healthy()
assert l.getFirst() == None
assert l.getLast() == None
assert l.size() == None
