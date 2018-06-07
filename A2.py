'''Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
'''
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(text)
matcher=re.finditer('b[a-zA-Z]*|B[a-zA-Z]*',text)
for m in matcher:
    print("Words starting with b or B are:{}".format(m.group()))
