N = int(input())
 
def smaller(number):
    for i in range(number+1):
        print(number-i, end=" ")
 
smaller(N)