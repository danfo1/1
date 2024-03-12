class Circulelist:
    class Node:
        __slots__='_elemento','_siguiente'
        def __init__(self,elemento,siguiente):
            self._elemento=elemento
            self._siguiente=siguiente
            self._head=self._Node(e,self._head)

    def __init__(self):
        self._tail=None
        self._size=0
    
    def __len__(self):
        return self._size

    def vacia(self):
        return self.__size==0

    def puhs(self,e):
        self._head=self._Node(e,self._head)
        self.__size+=1

    def first (self):
        if self.vacia():
            raise Empty('cola vacia')
        head=self._tail._next
        return head._elemento
    def dequeue(self):
        if self.vacia():
            raise Empty('cola vacia')
        oldhead=self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next==oldhead._next
        self._size-=1
        return oldhead._elemento
    def enqueue (self,e):
        newest=self._Node(e, None)
        if self.vacia():
            newest._next=self._tail._next
            self._tail._next=newest
            self._size +=1

    def rotate(self):
        if self._size>0:
            self._tail._next
            
