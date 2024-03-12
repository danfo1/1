class criptocesar:
    def __init__(self,shift):
        codificador=[None]*26
        decodificador=[None]*26
        for k in range (26):
            codificador[k]=chr((k+shift)%26+ord('A'))
            decodificador[k]=chr((k-shift)%26+ord('A'))
        self._encriptado=  ''.join(codificador)
        self._desencriptado=''.join(decodificador)
    def encriptrar(self,mensaje):
        return self.transformar(mensaje,self._encriptado)
    
    def desencriptrar(self,secreto):
        return self.transformar(secreto,self._desencriptado)
    
    def transformar(self,original,codigo):
        mensajeTexto=list(original)
        for k in range (len(mensajeTexto)):
            if mensajeTexto[k].isupper():
                j=ord(mensajeTexto[k])-ord('A')
                mensajeTexto[k]=codigo[j]
        return''.join(mensajeTexto)
if __name__=='__main__':
    cifrado=criptocesar(5)
    mensaje="CREAR UN MESAJE"
    codificado=cifrado.encriptrar(mensaje)
    print('secreto:',codificado)
    respuesta=cifrado.desencriptrar(codificado)
    print('mensaje:',respuesta)