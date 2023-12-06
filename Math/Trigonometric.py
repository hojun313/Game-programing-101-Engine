# 테일러 급수를 이용한 사인, 코사인, 탄젠트 함수 구현
PI = 3.141592653589793

# 각을 라디안으로 변환하는 함수
def degrees_to_radians(degrees):
    return degrees * (PI / 180.0)

# 사인 함수 구현
def my_sin(x):
    x = degrees_to_radians(x)  # 각을 라디안으로 변환
    result = 0.0
    term = x
    n = 1

    for i in range(10):
        result += term
        term *= -(x**2) / ((2 * n) * (2 * n + 1))
        n += 1

    return result

# 코사인 함수 구현
def my_cos(x):
    x = degrees_to_radians(x)  # 각을 라디안으로 변환
    result = 1.0
    term = 1.0
    n = 1

    for i in range(10):
        term *= -(x**2) / ((2 * n - 1) * (2 * n))
        result += term
        n += 1

    return result

# 탄젠트 함수 구현
def my_tan(x):
    return my_sin(x) / my_cos(x)

# 테스트 코드
if __name__ == "__main__":
    print(my_sin(30))
    print(my_cos(30))
    print(my_tan(30))

    print(my_tan(45))
    print(my_sin(110))