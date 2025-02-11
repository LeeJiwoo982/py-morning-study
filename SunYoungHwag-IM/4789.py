# 성공적인 공연 기획


## GPT 선생님

T = int(input())  # 테스트 케이스 개수

for tc in range(1, T+1):
    audience = list(map(int, input().strip()))  # 문자열을 숫자 리스트로 변환
    standing = 0  # 현재 박수치는 사람 수
    hire = 0  # 고용해야 하는 추가 인원 수

    for i, num in enumerate(audience):  # 문자열의 각 문자(숫자) 순회
        if standing < i:  # 현재 서 있는 사람이 i번째에서 필요한 최소 인원보다 적다면
            hire += (i - standing)  # 부족한 만큼 추가 인원 고용
            standing = i  # 추가 고용 후 박수치는 인원 증가
        standing += num  # 현재 인원에서 박수치는 사람 추가

    print(f"#{tc} {hire}")