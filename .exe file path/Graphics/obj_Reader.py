class ObjReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.vertices = []
        self.faces = []

    def load_obj(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    # 정점 데이터를 추출합니다.
                    vertex = list(map(float, line[2:].split()[:2]))  # 2D 객체이므로 x, y 좌표만 고려
                    self.vertices.append(vertex)
                elif line.startswith('f '):
                    # 면 데이터를 추출합니다.
                    face = [int(vertex.split('/')[0]) for vertex in line[2:].split()]
                    self.faces.append(face)

    def get_vertices(self):
        return self.vertices

    def get_faces(self):
        return self.faces

# 테스트 코드
if __name__ == "__main__":
    obj_reader = ObjReader("Graphics\ex.obj")
    obj_reader.load_obj()

    vertices = obj_reader.get_vertices()
    faces = obj_reader.get_faces()

    print("2D 정점 좌표:")
    for vertex in vertices:
        print(vertex)

    print("\n면 데이터:")
    for face in faces:
        print(face)