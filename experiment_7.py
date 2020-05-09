c=int(input("enter a positive number (less than 1000):  "))
count=0
for i in range(0,c):     
    for j in range(i,c):
        if i*i + j*j ==c:
            count=count+1
            print("pair",count)
            print([i,j])
