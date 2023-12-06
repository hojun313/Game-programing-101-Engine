from inputs import get_gamepad

def get_dualsense_controller_input():
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key":
                print(f"Button {event.ev_code} {'pressed' if event.ev_value == 1 else 'released'}")
            elif event.ev_type == "Absolute":
                print(f"Axis {event.ev_code} value: {event.ev_value}")

#임포트시 실행 방지
if __name__ == "__main__":
    get_dualsense_controller_input()