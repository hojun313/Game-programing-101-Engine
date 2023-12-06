def numerical_integral(f, a, b, n=1000):
    # 적분 구간을 균등하게 나누어줍니다.
    h = (b - a) / n

    # 초기값 설정
    integral_value = 0.0

    # 사다리꼴 규칙을 이용하여 적분 값을 계산합니다.
    for i in range(n + 1):
        x = a + i * h
        if i == 0 or i == n:
            integral_value += f(x)
        else:
            integral_value += 2 * f(x)

    integral_value *= h / 2

    return integral_value

def numerical_integral_2d(f, a, b, c, d, nx=1000, ny=1000):
    # 적분 구간을 균등하게 나누어줍니다.
    hx = (b - a) / nx
    hy = (d - c) / ny

    # 초기값 설정
    integral_value = 0.0

    # 사다리꼴 규칙을 이용하여 적분 값을 계산합니다.
    for i in range(nx + 1):
        for j in range(ny + 1):
            x = a + i * hx
            y = c + j * hy
            if i == 0 or i == nx:
                if j == 0 or j == ny:
                    integral_value += f(x, y)
                else:
                    integral_value += 2 * f(x, y)
            else:
                if j == 0 or j == ny:
                    integral_value += 2 * f(x, y)
                else:
                    integral_value += 4 * f(x, y)

    integral_value *= hx * hy / 4

    return integral_value

def numerical_integral_nd(f, a, b, n=1000):
    # 적분 구간을 균등하게 나누어줍니다.
    h = [(b[i] - a[i]) / n for i in range(len(a))]

    # 초기값 설정
    integral_value = 0.0

    # 사다리꼴 규칙을 이용하여 적분 값을 계산합니다.
    for i in range(n + 1):
        x = [a[j] + i * h[j] for j in range(len(a))]
        if i == 0 or i == n:
            integral_value += f(x)
        else:
            integral_value += 2 * f(x)

    integral_value *= h[0] / 2

    return integral_value

# 테스트 코드
if __name__ == "__main__":
    # f(x) = 3x^2 함수의 정적분을 구하는 예제
    f = lambda x: 3*x**2
    integral_value = numerical_integral(f, 0, 10)
    print(integral_value)

    # f(x, y) = 2x + 8xy + 2y 함수의 정적분을 구하는 예제
    f = lambda x, y: 2*x + 8*x*y + 2*y
    integral_value = numerical_integral_2d(f, 0, 1, 0, 1)
    print(integral_value)

    # f(x, y, z) = 2x + 3xy + y^3 + 2xz + z^2 함수의 정적분을 구하는 예제
    f = lambda x: 2*x[0] + 3*x[0]*x[1] + x[1]**3 + 2*x[0]*x[2] + x[2]**2
    integral_value = numerical_integral_nd(f, [0, 0, 0], [1, 1, 1])
    print(integral_value)