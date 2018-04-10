class filepalindrome:
    f=input("file name:") # entering file name
    with  open (f) as fp: # open file
        contents = fp.read()# read a file
        for en in contents.split('@'): #split based on @ create new line
            print(en) # print every line
            s2=en.lower()# convert to lower case
            s3=s2[::-1] # reverse a string
            if(s2==s3): # checking string before reverse and after reverse both are same or not
                print("palindrome")# if both are same it will print palindrome
            else:
                print("not palindrome") # if not same it will print not palindrome



