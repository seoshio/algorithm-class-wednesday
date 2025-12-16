# 0/1 배낭 문제 - 여행 짐 꾸리기

item = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
weight = [3, 1, 2, 2, 1]
value = [12, 10, 6, 7, 4]

n = len(items)

W = int(input("배낭 용량을 입력 하세요 : "))

# DP 테이블 생성
A = [[0] * (W + 1) for _ in range(n + 1)]

# Bottom-up 방식
for i in range(1, n + 1):
    for w in range(1, W + 1):
        if weight[i - 1] > w:
            A[i][w] = A[i - 1][w]
        else:
            val_with = value[i - 1] + A[i - 1][w - weight[i - 1]]
            val_without = A[i - 1][w]
            A[i][w] = max(val_with, val_without)

# 최대 만족도
max_value = A[n][W]

# 선택한 물건 역추적
selected_item = []
w = W

for i in range(n, 0, -1):
    if A[i][w] != A[i - 1][w]:
        selected_item.append(item[i - 1])
        w -= weights[i - 1]

selected_item.reverse()

print("최대 만족도:", max_value)
print("선택된 물건:", selected_item)
