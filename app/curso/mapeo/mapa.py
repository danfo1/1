

freq={}
filename = 'C:/Users/dsforero/Desktop/app/curso/mapeo/texto.txt'

for piece in open(filename).read().lower().split():
        word=''.join(c for c in piece if c.isalpha())
        if word:
                freq[word]=1+freq.get(word,0)
max_word=''
max_count=0
for(w,c) in freq.items():
        if c > max_count:
                max_word=w
                max_count=c 


print("La palabra más frecuente es:", max_word) 
print("Su número de ocurrencias es:", max_count)