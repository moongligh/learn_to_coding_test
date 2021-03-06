'''
  <문제> 문자열 재정렬
  알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
  이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한값을 이어서 출력합니다.

  입력조건: 첫째 줄에 하나의 문자열 S가 주어집니다.(1 <= S의 길이 <= 10000)
  
  출력조건: 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
'''

S = input()
num = 0
result = []

for x in S:
  if x.isalpha(): #알파벳인경우 리스트에 삽입
    result.append(x)
  else: #숫자인경우 따로 합하기
    num += int(x)

result.sort() #알파벳을 정렬하기

if num =!0: #숫자의 합이 0이 아니라면 리스트에 추가하기
  result.append(str(num)) 

print(''.join(result))