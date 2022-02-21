'''
  <문제> 두 배열의 원소 교체
  두 개의 배열 A와 B를 가지고 있습니다.
  두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
  최대 K번의 바꿔치기 연산을 수행하여 배열 A의 모든 원소의 합의 최댓값을 출력하시오.

  입력조건: 첫 번째 줄에 N, K가 공백을 기준으로 구분되어 입력됩니다.(1 <= n <= 100000, 0 <= K <= N)
  두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력됩니다.
  모든 원소는 10000000보다 작은 자연수입니다.
  세 번째 줄에 배열 B의 원소들이 공백을 기준으로 구분되어 입력됩니다.
  모든 원소는 10000000보다 작은 자연수입니다.
          
  출력조건: 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력합니다.
'''

N, K = map(int, input().split())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

arrayA.sort() #배열을 오름차순으로 정렬
arrayB.sort(reverse = True) #배열을 내림차순으로 정렬

for i in range(K): #K번만큼 반복하기
  if arrayA[i] < arrayB[i]: #원소 비교후 더 arrayB의 원소가 더 크면 두 원소를 교체
    arrayA[i], arrayB[i] = arrayB[i], arrayA[i]
  else: #arrayA의 원소가 더 클시 반복문을 탈출
    break

print(sum(arrayA))