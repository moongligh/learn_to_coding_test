'''
  <문제> 거스름 돈
  당신은 음식점의 계산을 도와주는 점원입니다. 카운터에는 사용할 500원, 100원 50원, 10원짜리 동전이 무수히 존재한다고 가정합니다. 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요.

  입력조건: 첫째 줄에 거슬러 줘야 할 돈 N이 주어집니다. (단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.)
  출력조건: 거슬러 줘야 할 돈 N의 동전 최소 개수를 출력합니다.
'''

N = int(input())
coins = [500, 100, 50, 10] #큰 화폐부터 처리하기위한 순서 리스트
result = 0

for coin in coins:
  result += N//coin #해당 화폐로 거슬러준 동전의 개수 더하기
  N = N%coin

print(result)