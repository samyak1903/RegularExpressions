'''Q.1- Extract the user id, domain name and suffix from the following email addresses. 
emails = "zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"
desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')] Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better." Q.3- Split the following irregular sentence into words 
sentence = "A, very very; irregular_sentence"
desired_output = "A very very irregular sentence"
'''
import re
l=[]
ch='y'
while ch.lower()=='y':
    email=input("Enter the email id:")
    t= tuple(re.split('\W', email))
    l.append(t)
    print(l)
    ch=input("Want to enter more mail id's? y/n")

