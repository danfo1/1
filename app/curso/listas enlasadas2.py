class linledStack:

    class Node:

        __slots__='_elmento','_siguiente'

    def __init__ (self,elemento,siguiente):
        self._elmento= elemento
        self._siguiente=siguiente
        self._head=self._Node(e,self._head)

def __init__ (self):
    self._head=None
    self.__size=0

def __len__(self):
    return self-__len__

def vacia(self):
    return self.__size==0

def puhs(self,e):
    self._head=self._Node(e,self._head)
    self.__size+=1

def top (self):
    if self.vacia():
        raise Empty('pila vacia')
    return self._head._elemento

def pop (self):

    if self.vacia():
        raise Empty('pila vacia')
    answer=self._head._elemento
    self._head=self._head._next
    self.__size -=1
    return answer