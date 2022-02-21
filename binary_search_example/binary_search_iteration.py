def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target: #찾은경우 중간점 인덱스 반환
      return mid
    elif array[mid] > target: #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인
      end = mid - 1
    else: #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인
      start = mid + 1
    
    return None

N, target = list(map(int, input().split())) #원소의 갯수와 target 값을 입력 받기
array = list(map(int, input().split()))

result = binary_search(array, target, 0, N - 1)
if result == None:
  print('원소가 존재하지 않습니다.')
else:
  print(result + 1)