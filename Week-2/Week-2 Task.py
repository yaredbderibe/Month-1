def sumFunction ( a, b ): 
    return a+b

print("The output of the Sum function is: " , sumFunction(2, 3))

print( "And here are the even numbers from 0 to 20: " , end="" )

for i in range(1,20,1):
    if i % 2 == 0:
        print( i , end=" ")


numbers = [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

x = numbers[0] 

for j in numbers:
    if j > x:  
        x = j  

print("The largest number from the list is", x)
