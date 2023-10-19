# 두 정수 입력
num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

# 연산 기호 입력
operator = input("사칙연산 기호를 입력하세요 (+, -, *, /): ")

# 사칙연산 수행 및 결과 출력
if operator == '+':
    result = num1 + num2
    print("덧셈 결과:", result)
elif operator == '-':
    result = num1 - num2
    print("뺄셈 결과:", result)
elif operator == '*':
    result = num1 * num2
    print("곱셈 결과:", result)
elif operator == '/':
    if num2 == 0:
        print("오류: 0으로 나눌 수 없습니다.")
    else:
        result = num1 / num2
        print("나눗셈 결과:", result)
else:
    print("오류: 지원하지 않는 연산 기호입니다.")
