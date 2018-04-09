class filepal:
    file=input("enter file name") #i am entering the file name through console
    lines=open(file,"r") #opening file for reading
    for s in lines: #for loop go through every line present in the file
        s1 = ''.join (e for e in s if e.isalnum ()) # isalnum() check alphabet or number.for loop go through every elememt and join method concate characters
        s2=s1.lower()#it will convert to lower case
        s3=s2[::-1]#it will reverse string
        if(s2==s3):# here i am checking string with after reverse
            print(s2)
            print("this line is palindrome")#if both same string and after reverse it will palindrome
        else:
            print("it is not palindrome")#if it not same it will print not palindrome



