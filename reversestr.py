class reversestr:
  def rev(s):
    s1=s.split(' ') # it will spilt line into words based on spaces
    s2=s1[::-1] # it reverse the words in string
    for i in s2: # for loop is used to concatenate the words
      print(i,end=' ') # end of word it will print spaces
  s=input("enter inut") # take the input as string
  rev(s) # calling method with argument
