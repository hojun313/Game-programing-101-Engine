import math
import numpy as np

def check_AABB_collision(rect1, rect2):
    """
    Axis-Aligned Bounding Box (AABB)를 사용하여 두 사각형 간의 충돌을 감지하는 함수

    Parameters:
    - rect1: (x1, y1, width1, height1) 형태의 튜플로 나타낸 첫 번째 AABB 정보
    - rect2: (x2, y2, width2, height2) 형태의 튜플로 나타낸 두 번째 AABB 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """
    # 두 사각형의 충돌 여부를 계산
    return (
        rect1[0] <= rect2[0] + rect2[2] and
        rect1[0] + rect1[2] >= rect2[0] and
        rect1[1] <= rect2[1] + rect2[3] and
        rect1[1] + rect1[3] >= rect2[1]
    )
        
def check_obb_collision(rect1, rect2):
    """
    Oriented Bounding Box (OBB)를 사용하여 두 사각형 간의 충돌을 감지하는 함수

    Parameters:
    - rect1: (x1, y1, width1, height1, angle1) 형태의 튜플로 나타낸 첫 번째 OBB 정보
    - rect2: (x2, y2, width2, height2, angle2) 형태의 튜플로 나타낸 두 번째 OBB 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """
    # 두 사각형의 중심 좌표
    center1 = (rect1[0] + rect1[2] / 2, rect1[1] + rect1[3] / 2)
    center2 = (rect2[0] + rect2[2] / 2, rect2[1] + rect2[3] / 2)

    # 두 사각형의 변 방향 벡터
    axis1 = np.array([math.cos(rect1[4]), math.sin(rect1[4])])
    axis2 = np.array([math.cos(rect2[4]), math.sin(rect2[4])])

    # 두 사각형의 변 벡터
    edges1 = [np.array([math.cos(rect1[4] + math.pi / 2), math.sin(rect1[4] + math.pi / 2)]),
              np.array([math.cos(rect1[4] - math.pi / 2), math.sin(rect1[4] - math.pi / 2)])]

    edges2 = [np.array([math.cos(rect2[4] + math.pi / 2), math.sin(rect2[4] + math.pi / 2)]),
              np.array([math.cos(rect2[4] - math.pi / 2), math.sin(rect2[4] - math.pi / 2)])]

    # 두 사각형의 중심 간의 벡터
    delta = np.array(center1) - np.array(center2)

    # 축으로 투영하여 겹침 확인
    for axis in [axis1, axis2] + edges1 + edges2:
        projection1 = [np.dot(np.array([rect1[i] - center1[0], rect1[i + 1] - center1[1]]), axis) for i in range(0, 8, 2)]
        projection2 = [np.dot(np.array([rect2[i] - center2[0], rect2[i + 1] - center2[1]]), axis) for i in range(0, 8, 2)]

        overlap = (
            max(projection1) >= min(projection2) and
            max(projection2) >= min(projection1)
        )

        if not overlap:
            return False

def check_moving_objects_collision(rect1, velocity1, rect2, velocity2):
    """
    두 개의 이동 중인 사각형 간의 충돌을 감지하는 함수

    Parameters:
    - rect1: (x1, y1, width1, height1) 형태의 튜플로 나타낸 첫 번째 사각형 정보
    - velocity1: (vx1, vy1) 형태의 튜플로 나타낸 첫 번째 사각형의 속도 정보
    - rect2: (x2, y2, width2, height2) 형태의 튜플로 나타낸 두 번째 사각형 정보
    - velocity2: (vx2, vy2) 형태의 튜플로 나타낸 두 번째 사각형의 속도 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """
    # 두 객체 간의 상대적인 속도 계산
    relative_velocity = np.array([velocity1[0] - velocity2[0], velocity1[1] - velocity2[1]])

    # 두 객체의 예측 위치 계산
    future_rect1 = (rect1[0] + velocity1[0], rect1[1] + velocity1[1], rect1[2], rect1[3])
    future_rect2 = (rect2[0] + velocity2[0], rect2[1] + velocity2[1], rect2[2], rect2[3])

    # 예측 위치에서의 충돌 여부 확인
    return check_AABB_collision(future_rect1, future_rect2)

def check_point_in_rect(point, rect):
    """
    주어진 점이 주어진 사각형 내부에 있는지 확인하는 함수

    Parameters:
    - point: (x, y) 형태의 튜플로 나타낸 점의 위치
    - rect: (x, y, width, height) 형태의 튜플로 나타낸 사각형 정보

    Returns:
    - 점이 사각형 내부에 있으면 True, 그렇지 않으면 False를 반환
    """
    return (
        rect[0] <= point[0] <= rect[0] + rect[2] and
        rect[1] <= point[1] <= rect[1] + rect[3]
    )

def check_point_in_circle(point, circle):
    """
    주어진 점이 주어진 원 내부에 있는지 확인하는 함수

    Parameters:
    - point: (x, y) 형태의 튜플로 나타낸 점의 위치
    - circle: (x, y, radius) 형태의 튜플로 나타낸 원의 정보

    Returns:
    - 점이 원 내부에 있으면 True, 그렇지 않으면 False를 반환
    """
    return np.linalg.norm(np.array(point) - np.array(circle[:2])) <= circle[2]

def check_circle_collision(circle1, circle2):
    """
    두 개의 원 간의 충돌을 감지하는 함수

    Parameters:
    - circle1: (x1, y1, radius1) 형태의 튜플로 나타낸 첫 번째 원의 정보
    - circle2: (x2, y2, radius2) 형태의 튜플로 나타낸 두 번째 원의 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """
    return np.linalg.norm(np.array(circle1[:2]) - np.array(circle2[:2])) <= circle1[2] + circle2[2]

def check_segment_circle_collision(segment, circle):
    """
    선분과 원 간의 충돌을 감지하는 함수

    Parameters:
    - segment: (x1, y1, x2, y2) 형태의 튜플로 나타낸 선분의 정보
    - circle: (x, y, radius) 형태의 튜플로 나타낸 원의 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """
    # 선분의 양 끝점과 원의 중심 간의 거리를 계산
    distance1 = np.linalg.norm(np.array(segment[:2]) - np.array(circle[:2]))
    distance2 = np.linalg.norm(np.array(segment[2:]) - np.array(circle[:2]))

    # 선분의 양 끝점이 원 내부에 있는 경우
    if distance1 <= circle[2] or distance2 <= circle[2]:
        return True

    # 선분의 양 끝점이 원의 반지름을 기준으로 반대쪽에 있는 경우
    if distance1 >= circle[2] and distance2 >= circle[2]:
        # 선분의 양 끝점과 원의 중심을 지나는 직선의 방정식 계수 계산
        a = segment[3] - segment[1]
        b = segment[0] - segment[2]
        c = segment[2] * segment[1] - segment[0] * segment[3]

        # 선분의 양 끝점과 원의 중심을 지나는 직선과 원의 중심 간의 거리 계산
        distance = abs(a * circle[0] + b * circle[1] + c) / math.sqrt(a * a + b * b)

        # 선분의 양 끝점과 원의 중심 간의 거리가 원의 반지름보다 작은 경우
        if distance <= circle[2]:
            return True

def check_rect_circle_collision(rect, circle):
    """
    사각형과 원 간의 충돌을 감지하는 함수

    Parameters:
    - rect: (x, y, width, height) 형태의 튜플로 나타낸 사각형 정보
    - circle: (x, y, radius) 형태의 튜플로 나타낸 원의 정보

    Returns:
    - 충돌이 발생하면 True, 그렇지 않으면 False를 반환
    """

    # 사각형의 각 꼭지점을 원과의 충돌 검사
    for point in [(rect[0], rect[1]), (rect[0] + rect[2], rect[1]), (rect[0], rect[1] + rect[3]), (rect[0] + rect[2], rect[1] + rect[3])]:
        if check_point_in_circle(point, circle):
            return True

    # 원의 중심을 사각형과의 충돌 검사
    if check_point_in_rect(circle[:2], rect):
        return True

    # 사각형의 각 변을 원과의 충돌 검사
    for edge in [(rect[0], rect[1], rect[0] + rect[2], rect[1]), (rect[0] + rect[2], rect[1], rect[0] + rect[2], rect[1] + rect[3]), (rect[0], rect[1] + rect[3], rect[0] + rect[2], rect[1] + rect[3]), (rect[0], rect[1], rect[0], rect[1] + rect[3])]:
        if check_segment_circle_collision(edge, circle):
            return True

    return False