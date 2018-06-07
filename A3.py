'''Q.3- Split the following irregular sentence into words 
sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence'''
import re
sentence = "A, very very; irregular_sentence"
print(sentence)
new_sentence=re.sub('\W',' ',sentence)
print(new_sentence)
l=re.split(' ',new_sentence)
s=''
for i in l:
    if i!=' ':
        s+=i+' '
print(s)
