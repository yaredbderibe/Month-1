def sumFunction ( a, b ): 
    return a+b

print("The output of the Sum function is: " , sumFunction(2, 3))

print( "And here are the even numbers from 0 to 20: " , end="" )

for i in range(1,20,1):
    if i % 2 == 0:
        print( i , end=" ")