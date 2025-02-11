T = int(input())
 
numbers = []
for i in range(T):
    values = list(map(int, input().split()))
    numbers.append(values)
 
# for i in range(T):
#   print(f'#{i+1} {round(sum(numbers[i])/len(numbers[i]))}')
 
def mean_fun(inputs):
    mean_answers =[]
    for i in range(len(inputs)):
        mean_answers.append('#'+str(i+1)+" "+str(round(sum(inputs[i])/(len(inputs[i])))))
    return "\n".join(mean_answers)
 
print(mean_fun(numbers))