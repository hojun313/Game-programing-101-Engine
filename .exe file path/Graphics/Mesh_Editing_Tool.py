import math

class MeshEditingTool:
    def __init__(self, mesh):
        self.mesh = mesh

    def translate(self, translation_vector):
        # 주어진 벡터만큼 메시의 각 꼭짓점을 이동
        for i in range(len(self.mesh.vertices)):
            for j in range(2):
                self.mesh.vertices[i][j] += translation_vector[j]

    def scale(self, scale_factor):
        # 주어진 스케일 비율로 메시의 각 꼭짓점을 조정
        for i in range(len(self.mesh.vertices)):
            for j in range(2):
                self.mesh.vertices[i][j] *= scale_factor

    def rotate(self, rotation_angle):
        # 주어진 회전 각도로 메시의 각 꼭짓점을 회전
        # 간단한 2D 회전 행렬 사용
        for i in range(len(self.mesh.vertices)):
            x = self.mesh.vertices[i][0]
            y = self.mesh.vertices[i][1]
            new_x = x * math.cos(rotation_angle) - y * math.sin(rotation_angle)
            new_y = x * math.sin(rotation_angle) + y * math.cos(rotation_angle)
            self.mesh.vertices[i] = [new_x, new_y]

    def apply_deformation(self, deformation_function):
        # 사용자 정의 변형 함수를 메시에 적용
        self.mesh.vertices = deformation_function(self.mesh.vertices)

# 테스트 코드
class Mesh:
    def __init__(self, vertices):
        self.vertices = vertices

# MeshEditingTool 클래스와 간단한 Mesh 클래스 정의 후에 테스트 코드 작성
if __name__ == "__main__":
    # 테스트할 Mesh 객체 생성
    initial_vertices = [[1, 1], [2, 2], [3, 3]]
    test_mesh = Mesh(initial_vertices)

    # MeshEditingTool 객체 생성
    mesh_editor = MeshEditingTool(test_mesh)
    print("Mesh vertices:", test_mesh.vertices)

    # 이동 테스트
    translation_vector = [1, 2]
    mesh_editor.translate(translation_vector)
    print("이동 후 Mesh vertices:", test_mesh.vertices)

    # 스케일 테스트
    scale_factor = 2
    mesh_editor.scale(scale_factor)
    print("스케일 후 Mesh vertices:", test_mesh.vertices)

    # 회전 테스트
    rotation_angle = math.radians(45)  # 45도를 라디안으로 변환
    mesh_editor.rotate(rotation_angle)
    print("회전 후 Mesh vertices:", test_mesh.vertices)
    mesh_editor.rotate(rotation_angle)
    print("2번째 회전 후 Mesh vertices:", test_mesh.vertices)

    # 변형 함수 적용 테스트 (임의의 변형 함수 예시)
    def deformation_function(vertices):
        for i in range(len(vertices)):
            for j in range(2):
                vertices[i][j] = vertices[i][j] ** 2  # 각 좌표값을 제곱
        return vertices

    mesh_editor.apply_deformation(deformation_function)
    print("변형 함수 적용 후 Mesh vertices:", test_mesh.vertices)