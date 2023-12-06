class VectorOperations:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2

    # 벡터 덧셈
    def add(self):
        return [self.vector1[0] + self.vector2[0], self.vector1[1] + self.vector2[1]]

    # 벡터 뺄셈
    def subtract(self):
        return [self.vector1[0] - self.vector2[0], self.vector1[1] - self.vector2[1]]

    # 벡터 스칼라 곱셈
    def multiply(self, scalar):
        return [self.vector1[0] * scalar, self.vector1[1] * scalar]

    # 벡터 스칼라 나눗셈
    def divide(self, scalar):
        return [self.vector1[0] / scalar, self.vector1[1] / scalar]

    # 벡터의 내적
    def dot_product(self):
        return self.vector1[0] * self.vector2[0] + self.vector1[1] * self.vector2[1]
    
    # 벡터의 외적 (2차원 벡터이기에 z값이 반환된다)
    def cross_product(self):
        return self.vector1[0] * self.vector2[1] - self.vector1[1] * self.vector2[0]
    
    def is_parallel(self):
        return self.cross_product() == 0
    
    def is_orthogonal(self):
        return self.dot_product() == 0
    
    def is_same_direction(self):
        return self.dot_product() > 0
    
    def is_opposite_direction(self):
        return self.dot_product() < 0

# 테스트 코드
if __name__ == "__main__":
    v1 = [1, 2]
    v2 = [3, 4]
    vector_operations = VectorOperations(v1, v2)

    print("벡터 덧셈:", vector_operations.add())
    print("벡터 뺄셈:", vector_operations.subtract())
    print("벡터 스칼라 곱셈:", vector_operations.multiply(3))
    print("벡터 스칼라 나눗셈:", vector_operations.divide(3))
    print("벡터의 내적:", vector_operations.dot_product())
    print("벡터의 외적:", vector_operations.cross_product())
    print("벡터의 평행 여부:", vector_operations.is_parallel())
    print("벡터의 직교 여부:", vector_operations.is_orthogonal())
    print("벡터의 같은 방향 여부:", vector_operations.is_same_direction())
    print("벡터의 반대 방향 여부:", vector_operations.is_opposite_direction())