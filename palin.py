s="i race car"
s1=''.join(e for e in s if e.isalnum())
l=len(s1)
r=''
s2=s1.lower()
for i in range(l-1,-1,-1):
 r+=s2[i]
if(s2==r):
 print("given string is palindrome")
elif(s==0):
    print("given string is palindrome")
elif(s2!=r):
    print("not palindrome")
