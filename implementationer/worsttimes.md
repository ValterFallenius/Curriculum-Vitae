# Worst case times for methods in LinkedList-class

Let n be the number of elements in the list. Let the worst case time for a given method W<sub>methodX</sub> = function(n) represent the maximum amount of elementary opperations that is executed if the method is called. Elementary operations will differ between every method.

O() represents the big ordo notation

### 1: addFirst(self, value):

In this method we chose the elementary operation to be assignments like obj = _ListElement(value). The maximum amount of of operations is W<sub>addFirst</sub>(n) = konstant = 5. 

W<sub>addFirst</sub>(n) &isin; O(1)

### 2: addLast(self, value):

In this method we chose the elementary operation  as assignments like obj = _ListElement(value). The maximum amount of of operations is W<sub>addLast</sub>(n) = konstant = 9

W<sub>addLast</sub>(n) &isin; O(1)

### 3: getFirst(self):

In this method we chose the elementary operation as comparisons like self._first == None. The maximum amount of of operations is W<sub>getFirst</sub>(n) = konstant = 1

W<sub>getFirst</sub>(n) &isin; O(1)

### 4: getLast(self):

In this method we chose the elementary operation as comparisons like self._last == None. The maximum amount of of operations is W<sub>getLast</sub>(n) = konstant = 1

W<sub>getLast</sub>(n) &isin; O(1)

### 5: getIndex(self, index):

In this method we chose the elementary operation as assignments like item = item.next. The maximum amount of of operations is W<sub>getIndex</sub>(n) = n + 2 &prop; n

W<sub>getIndex</sub>(n) &isin; O(n)

### 6: removeFirst(self):

In this method we chose the elementary operation to be assignments like first = self._first. The maximum amount of of operations is W<sub>removeFirst</sub>(n) = konstant = 5

W<sub>removeFirst</sub>(n) &isin; O(1)

### 7: clear(self):

In this method we chose the elementary operation as assignments like self._first = None. The maximum amount of of operations is W<sub>clear</sub>(n) = konstant = 3

W<sub>clear</sub>(n) &isin; O(1)

### 8: size(self):

In this method we chose the elementary operation as comparisons like self._last == None. The maximum amount of of operations is W<sub>size</sub>(n) = konstant = 1

W<sub>size</sub>(n) &isin; O(1)

### 9: string(self):

In this method we chose the elementary operation as assignments like string= "[". The maximum amount of of operations is W<sub>string</sub>(n) = 2n + 5 &prop; 2n

W<sub>string</sub>(n) &isin; O(n)

### Conclusion:

The only two methods which were dependant on time were getIndex and string, of these two the string method was a bit slower. And therefore the slowest method in the class.
