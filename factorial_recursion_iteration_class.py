#############################################################################
#  시스템 스택 호출과 재귀함수를 이용한 팩토리얼 계산 콘솔 인터렉티브 프로그램 
#  작성자: 김현서
#  작성일: 2025-09-22

#############################################################################




def factorial_iter(n):
    result = 1
    for k in range(2, n+1):
        result = result * k
    return result



def factorial_rec(n):
    # 재귀 기반 n! -> 재귀함수 정의

    # 1. base case (재귀호풀 종료 조건)
    if n == 1:
        return 1
    
    # 2. 재귀 분할 호출
    return n * factorial_rec(n-1)

# 과제 : 메인함수에 상단 조건 포함시켜 실행까지.. 자세한 건 목요일 사캠에 공지함.

if __name__ == "__main__":
    n = int(input("\n정수를 입력하세요: ").strip())
    print(f"반복문 기반: {factorial_iter(n)}")
    try:
        print(f"재귀 기반: {factorial_rec(n)}")
    except RecursionError:
        print("입력값이 너무 커서 재귀 계산은 불가능합니다.")

    # main()
