# 연월일 달력
T=int(input())
val={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for i in range(1, T+1):
    date=input()
    year, month, day = map(int, [date[:4], date[4:6], date[6:]])

    if 1 <= day <= val.get(month, 0):
        print(f"#{i} {year:04}/{month:02}/{day:02}")
    else:
        print(f'#{i} -1')

    # year, month, day = date[:4], date[4:6], date[6:]
    # if int(day) <= val.get(int(month), False) and int(day) >=1:
    #     print(f'#{i} {year}/{month}/{day}')
    # day=date[-2:]
    # month=date[-4:-2]
    # year=date[:4]