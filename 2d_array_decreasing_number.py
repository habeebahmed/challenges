def chaneRange(arr,start,end,number):
    for i in range(start,end):
        for j in range(start,end):
            arr[i][j] = number

no=5
count = 0
temp = 0
arr = [[0 for x in range(2*no-1)] for y in range(2*no-1)] 
for n in range(no,0,-1):
    temp = 2*n-1+count
    chaneRange(arr,count,temp,n)
    count +=1
    
    
for i in range(2*no-1):
    for j in range(2*no-1):
        print('{}\t'.format(arr[i][j]),end=' ')
    print(end='\n')
    
