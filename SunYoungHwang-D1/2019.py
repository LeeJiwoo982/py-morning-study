T = int(input())
 
def dou_ble(num):
    results =[]
    for i in range(num+1):
        results.append(str(2**i))
    return " ".join(results)
 
print(dou_ble(T))