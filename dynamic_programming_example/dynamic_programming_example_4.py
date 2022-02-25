'''
  <문제> 금광
  N x M 크기의 금광이 있습니다.
  금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
  채굴자는 첫 번째 열부터 출발하며, 이후에 M - 1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하시오.

  입력조건: 첫째 줄에 테스트 케이스 T가 출력됩니다. (1 <= T <= 1000)
  매 테스트 케이스 첫째 줄에 N과 M이 공백으로 구분되어 입력됩니다. (1 <= N, M <= 20)
  둘째 줄에 N x M개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다.
  (1 <= 각 위치에 매장된 금의 개수 <= 100)
  
  출력조건: 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다.
  각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
'''
for tc in range(int(input())): #입력받은 테스트 케이스만큼 반복
  N, M = map(int, input().split())
  array = list(map(int, input().split()))

  dp = [] #다이나믹 프로그래밍을 위한 DP 테이블 초기화
  index = 0
  for i in range(N):
    dp.append(array[index: index + M])
    index += M

  for j in range(1, M): #다이나믹 프로그래밍 진행
    for i in range(N):
      #왼쪽 위에서 오는 경우
      if i == 0: left_up = 0
      else: left_up = dp[i - 1][j - 1]

      #왼쪽 아래에서 오는 경우
      if i == N - 1: left_down = 0
      else: left_down = dp[i + 1][j - 1]

      #왼쪽에서 오는 경우
      left = dp[i][j-1]

      #현재 금의 양 + 현재 위치로 올수있는 경우중에 가장 금이 많은 수
      dp[i][j] = max(left_up, left_down, left) + dp[i][j]

  result = 0
  
  #모든 행의 맨끝 인덱스를 비교하여 가장큰 값을 결과로 출력
  for i in range(N):
    result = max(result, dp[i][M - 1])

  print(result)