'''
  <문제> 미로 탈출
  동빈이는 N x M 크기의 직사각형 형태의 미로에 갇혔습니다.
  미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 합니다.
  동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있습니다.
  이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있습니다.
  미로는 반드시 탈출할 수 있는 형태로 제시됩니다.
  이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하세요.
  칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산합니다.

  입력조건: 첫째 줄에 두정수 N, M(4 <= N, M <= 200)이 주어집니다.
  다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어집니다.
  각각의 수들은 공백 없이 붙어서 입력으로 제시됩니다.
  또한 시작 칸과 마지막 칸은 항상 1입니다.
  
  출력조건: 첫재 줄에 최소 이동 칸의 개수를 출력합니다.
'''

def bfs(x, y, count):
  if x <= -1 or x >= N or y <= -1 or y >= M:
    count -= 1
    return count

  if x == N and y == M:
    return count
  elif miro[x][y] == 1:
    miro[x][y] = 0
    dfs(x+1, y, count)
    dfs(x, y+1, count)
    dfs(x-1, y, count)
    dfs(x, y-1, count)
    count += 1
    return count

N, M = map(int, input().split())
miro = []
for i in range(N):
  miro.append(list(map(int, input())))

count = 0
result = dfs(0, 0, count)

print(result)