T = int(input())
 
numbers = []
for i in range(T):
    numbers.append(input())
 
def calender(args):
    for i in range(len(args)):
        if int(str(args[i][4:6])) in [1,3,5,7,8,10,12]:
            if 1<=int(str(args[i][6:]))<=31:
                print("#"+str(i+1)+" "+str(args[i][:4])+"/"+str(args[i][4:6])+"/"+str(args[i][6:]))
            else:
                print("#"+str(i+1)+" "+"-1")
        elif int(str(args[i][4:6])) in [4,6,9,11]:
            if 1<=int(str(args[i][6:]))<=30:
                print("#"+str(i+1)+" "+str(args[i][:4])+"/"+str(args[i][4:6])+"/"+str(args[i][6:]))
            else:
                print("#"+str(i+1)+" "+"-1")
        elif int(str(args[i][4:6])) == 2:
            if 1<=int(str(args[i][6:]))<=28:
                print("#"+str(i+1)+" "+str(args[i][:4])+"/"+str(args[i][4:6])+"/"+str(args[i][6:]))
            else:
                print("#"+str(i+1)+" "+"-1")
        else:
            print("#"+str(i+1)+" "+"-1")
 
calender(numbers)