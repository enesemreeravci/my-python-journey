# Fibonnacci Sequence
# enter a number : 100, and program should print 0,1,1,2,3,5,8,13,21,34,55,89
# so a = 0 and b = 1 and next will be a+b = next


number = int(input("Enter a number: "))

a = 0 # first value of sequence
b = 1 # second value of sequence
seq = [] # an array to store fibonacci numbers

print("Fibonacci Sequence: ")

while(a < number): # loop will work as long as our input greate than a which is 0
    seq.append(a) # i couldnt find to any way to write numbers in one line except this one. 
    next_value = a + b  #Basiaclly program stores fibonacci numbers in an array which i called seq[]
    a = b
    b = next_value  # every time we have to check/sum with previous number so i find this method 
print(seq); # printing all fibonacci sequences as an array. 
