T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A=[]
    B=[]
    C=[]
    # bus = {'A':[], 'B':[], 'C':[]}
    for i in range(N):
        arr = list(map(int, input().split()))
        A.append(arr[0])
        B.append(arr[1])
    P = int(input())
    for i in range(P):
        C.append(int(input()))
    
    max_C = max(C)
    cnt_arr = [0] * (max_C+1)

    nA = len(A)
    for i in range(nA):
        for j in range(A[i], B[i]+1):
            if j <= max_C:
                cnt_arr[j]+=1
    # print(cnt_arr)
    print(f"#{tc} ", end='')
    for i in C:
        print(f"{cnt_arr[i]} ", end='')
    print('')