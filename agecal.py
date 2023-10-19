from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    # 현재 날짜 가져오기
    current_date = datetime.now()
    
    # 사용자의 생년월일로 날짜 생성
    birth_date = datetime(birth_year, birth_month, birth_day)
    
    # 나이 계산
    age = current_date.year - birth_date.year
    
    # 생일이 지났는지 확인
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

# 사용자로부터 생년월일 입력 받기
birth_year = int(input("태어난 년도를 입력하세요: "))
birth_month = int(input("태어난 월을 입력하세요: "))
birth_day = int(input("태어난 날짜를 입력하세요: "))

# 나이 계산
age = calculate_age(birth_year, birth_month, birth_day)

# 결과 출력
print(f"만 나이는 {age}세입니다.")
