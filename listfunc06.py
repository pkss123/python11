# .sort() 는 내부 요소를 크기가 작을수록 0번에 가깝게 재배치해줍니다
# .reverse() 는 내부 요소를 인덱스번호 역순으로 재배치해줍니다
from audioop import reverse
from listfunc02 import score
score = [88, 95, 70, 100, 99]
score.sort() # 오름차순 정렬
print(score)
score.reverse() # sort사용후 reverse 사용시 큰 숫자가 왼쪽
print(score)

# .sort(reverse=True) 로 정렬시 오름차순이 아닌 내림차순 정렬
score = [24, 35, 22, 13, 55, 79]
score.sort(reverse=True)
print(score)