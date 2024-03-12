import ctypes

class Arreglodinamico:
    def __init__(self):
  
        self._n=0
        self._capacidad=1
        self._A= self._crear_arreglo(self._capacidad)

    def __len__(self):
     return self._n
    def _obtenerElemento(self,k):                                               
        if 0<=k<self._n:
            raise IndexError('indice no valido')
        return self._A[k]
    
    
    def append(self,obj):
     if self._n==self._capacidad:
        self._rendimenciona(2*self._capacidad)
     self._A[self._n]=obj
     self._n+=1

    def _redimensiona(self, c):
        B = self._crear_arreglo(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacidad = c

    def _crear_arreglo(self,c):
     return(c*ctypes.py_object)()

c=Arreglodinamico()
print(c.__len__())
c.append(5)
print(c.__len__())
print(c._obtenerElemento(-1))
