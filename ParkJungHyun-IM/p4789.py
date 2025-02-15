def applause(arr, N):
    cnt=0 # 필요한 사람 수 합
    sum=0 # 해당 index 이전까지 사람 수 합
    for i in range(N):
        if arr[i] != 0:
            if i<=sum:
                sum+=arr[i]
            else:
                cnt+=i-sum
                # sum+=(arr[i]+cnt)
                # 이건 왜 안될까?
                # sum = sum + (arr[i] + (i -sum))
                # 안되지... cnt에 하나만 들어간게 아니잖아
                # cnt = i-sum이 아니라
                # cnt += i-sum이기 때문에 틀린 것!
                sum = arr[i] + i
    return cnt

T = int(input())
for tc in range(1, T+1):
    # people = input()
    # arr = []
    # for p in people:
    #     arr.append(int(p))
    arr = list(map(int, input())) # 문자열로 받은 애를 순회하면서 int해서 list화
    print(f"#{tc} {applause(arr, len(arr))}")