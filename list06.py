# 이차원 데이터 처리 예시
# 아파트 한 동에 대해서 신문을 배달할지 말지에 대해서
# 판단할 수 있는 반복문 작성
rooms = [[101,102,103,104],
        [201,202,203,204],
        [301,302,303,304],
        [401,402,403,404]]
nodeliver = [102,204,303,401]

for floor in rooms:
    for room in floor:
        if room not in nodeliver:
            print("%d호에 신문을 배달했습니다" % room)
        else:
            print("요금 미납 세대 %d호 입니다" % room)