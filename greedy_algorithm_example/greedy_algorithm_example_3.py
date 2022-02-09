'''
  <문제> 곱하기 혹은 더하기
  각 자리가 숫자(0부터9)로만 이루어진 문자열 S가주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

  입력조건: 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1 <= S의 길이 <= 20)
  출력조건: 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
'''

S = input()
result = int(S[0]) #시작시 문자열 S의 첫번째 숫자를 사용하기위한 초기화

for i in range(1, len(S)):
  num = int(S[i])
  
  if num <= 1 or result <= 1: #수가 0 또는 1이라 곱연산이 이득이 없는경우 합하기
    result += num
  else:
    result *= num

print(result)