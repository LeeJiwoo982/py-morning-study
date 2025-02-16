def turn_onoff(switches, idx):
    '''스위치 상태 변경 '''
    # 0이면 1로, 1이면 0으로
    switches[idx] = 1 - switches[idx]

def male_swc(switches, num):
    '''남학색 스위치
    자기가 받은 수의 배수를 바꾼다
    for문에서 레인지 범위 조절로 깔끔하게 가능'''
    for i in range(num-1, len(switches), num):
        turn_onoff(switches, i)

def female_swc(switches, num):
    '''여학생 스위치
    자기가 받은 수의 스위치 중심으로 좌우 대칭인 게 가장 많은 구간에 속한 번호 모두 바꾸기
    최소 자기자신 최대 전체'''
    idx = num -1
    turn_onoff(switches, idx)   #자기자신은 먼저 바꾸고
    
    left, right = idx-1, idx+1  #좌우 대칭인지 찾기
    while left >= 0 and right<len(switches) and switches[left] == switches[right]:
    # 좌 인덱스는 0보다 크고, 우 인덱스는 총길이보다 작게
    # 스위치의 좌 우 값이 같은 걸 모두 충족
        turn_onoff(switches, left)
        turn_onoff(switches, right)
        # 충족하면 스위치 바꾸고
        left -=1
        right +=1
        # 좌는 -1, 우는 +1
        #while 조건에 모든 경우를 만족하게 설정

N = int(input())    #스위치 개수
switches = list(map(int, input().split()))  # 스위치 상태
students = int(input())     # 학생 수

for _ in range(students):
    sex, num = map(int, input().split())    # 학생정보:성별, 스위치번호
    if sex == 1:    #남학생 경우
        male_swc(switches, num)
    else:   #여학생 경우
        female_swc(switches, num)

for i in range(0, N, 20):   #0에서 N까지 뽑는데 20단위로
    print(*switches[i:i+20])    #i=0 0~20, i=20 20~40