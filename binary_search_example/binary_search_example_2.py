'''
  <문제> 정렬된 배열에서 특정 수의 개수 구하기
  N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
  이때 이 수열에서 X가 등장하는 횟수를 계산하세요.
  예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 X = 2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
  (단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간초과 판정을 받습니다.)

  입력조건: 첫째 줄에 N과 정수 형태로 공백으로 구분되어 입력됩니다.
  (1 <= N <= 1000000), (-10^9 <= X <= 10^9)
  둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다.
  (-10^9 <= 각 원소의 값 <= 10^9)
    
  출력조건: 수열의 원소 중에서 값이 X인 원소의 개수를 출력합니다.
  단, 값이 X인 원소가 하나도 없다면 -1을 출력합니다.
'''
from bisect import bisect_left, bisect_right

#값이 left_value ~ right_value의 범위 이내의 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

N, X = map(int, input().split())
array = list(map(int, input().split()))

result = count_by_range(array, X, X)

if result == 0: #값이 X인 원소가 존재하지 않는경우 -1을 출력
  print(-1)
else:
  print(result)