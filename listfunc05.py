# 리스트 내부의 요소 유무 조회시 in, not in을 사용합니다
# 요소 in 리스트 -> 요소가 리스트 내에 내장된 경우 True 아니면 False
# 요소 not in 리스트 -> 위와 반대로True ,False 출력

answer = input("결제를 진행하시겠습니까")
if answer in ["ok", "yes", "응","ㅇㅋ"," ㄱㄱ", "네", "예"]:
    print("결제가 완료되었습니다")
else:
    print("안녕히가세요")