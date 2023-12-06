class RigidBody:
    def __init__(self, x, y, width, height, velocity_x=0, velocity_y=0, mass=1.0, friction=0.1, angle=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.mass = mass
        self.friction = friction
        self.angle = angle

    def apply_force(self, force_x, force_y):
        acceleration_x = force_x / self.mass
        acceleration_y = force_y / self.mass
        self.velocity_x += acceleration_x
        self.velocity_y += acceleration_y

    def apply_impulse(self, torque):
        angular_acceleration = torque / self.mass
        self.angle += angular_acceleration

    def update(self, is_friction = False):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # 간단한 마찰력 모델
        if self.velocity_x != 0 and is_friction:
            friction_force_x = -1 * self.friction * self.velocity_x
            self.apply_force(friction_force_x, 0)

        if self.velocity_y != 0 and is_friction:
            friction_force_y = -1 * self.friction * self.velocity_y
            self.apply_force(0, friction_force_y)

        self.angle %= 360
        self.angle += self.velocity_x

# 테스트 코드
if __name__ == "__main__":
    rigid_body = RigidBody(0, 0, 10, 10, 2, 2, 1, 0.1)
    print("질량이 1인 RigidBody 객체 생성:", rigid_body.__dict__)

    rigid_body.apply_force(10, 10)
    print("10, 10 크기의 힘을 가함:", rigid_body.__dict__)

    rigid_body.update(1)
    print("1초 후:", rigid_body.__dict__)