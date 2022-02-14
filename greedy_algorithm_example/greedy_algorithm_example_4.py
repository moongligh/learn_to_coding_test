'''
  <문제> 모험가 길드
  한 마을에 모험가 N명이 있습니다.
  모험가 길드에서는 N명의 모험가를 대상으로 '공포도'를 측정했는데, '공포도'가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있습니다.
  여행을 떠날 수 있는 그룹 수의 최대값을 구하시오.

  입력조건: 첫째 줄에 모험가의 수 N이 주어집니다.(1<= N <= 100000)
  둘째 줄에 각 모험가의 공포도의 값을 N이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.

  출력조건: 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.
'''
N = int(input())
S = list(map(int, input().split()))
S.sort() #그룹을 최대값으로 구하기위해서 공포도가 낮은 순서대로 정렬

result = 0
party = 0 #공포도 비교를위한 그룹인원 카운트

for i in range(N):
  party += 1

  if party >= S[i]:
    result += 1
    party = 0

print(result)
