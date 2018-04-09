class maxsub:
 lst=[2,1,-3,4,-1,2,1,-5,4]

 def some(lst):
    sum = 0
    max = 0
    for i in lst:
        sum=sum+i
        if(sum>max):
            max=sum
    print(max)

 some(lst)
