# 수치미분 함수
def numerical_derivative(f, x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

# 수치미분 함수 (2차원 함수)
def numerical_derivative_2d(f, x, y, h=1e-5):
    return (f(x+h, y+h) - f(x-h, y-h)) / (2*h)

# 수치미분 함수 (다변수 함수)
def numerical_derivative_nd(f, x, h=1e-5):
    grad = [0.0] * len(x)

    for i in range(len(x)):
        tmp_val = x[i]
        x[i] = tmp_val + h
        fx1 = f(x)

        x[i] = tmp_val - h
        fx2 = f(x)

        grad[i] = (fx1 - fx2) / (2 * h)

        x[i] = tmp_val

    return grad

# 테스트 코드
if __name__ == "__main__":
    # f(x) = x^2 함수의 도함수를 구하는 예제
    f = lambda x: x**2
    df = numerical_derivative(f, 3.0)
    print(df)

    # f(x, y) = 2x + 3xy + y^3 함수의 도함수를 구하는 예제
    f = lambda x, y: 2*x + 3*x*y + y**3
    df_x = numerical_derivative_2d(f, 1.0, 2.0)
    df_y = numerical_derivative_2d(f, 1.0, 2.0)
    print(df_x, df_y)

    # f(x, y, z) = 2x + 3xy + y^3 + 2xz + z^2 함수의 도함수를 구하는 예제
    f = lambda x: 2*x[0] + 3*x[0]*x[1] + x[1]**3 + 2*x[0]*x[2] + x[2]**2
    df = numerical_derivative_nd(f, [1.0, 2.0, 3.0])
    print(df)