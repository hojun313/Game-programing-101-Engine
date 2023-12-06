import numpy as np
import librosa

class SpatialAudio:
    def __init__(self, num_channels):
        # 초기화 메서드
        self.num_channels = num_channels
        self.audio_data = None

    def load_audio_data(self, audio_file):
        # 오디오 데이터를 불러오는 메서드
        self.audio_data, _ = librosa.load(audio_file, sr=None, mono=True)

    def apply_2d_panning(self, azimuth_angle):
        # 2차원 패닝을 적용하는 메서드
        # 입력 오디오 데이터의 길이를 확인
        num_samples = len(self.audio_data)
        
        # 좌우 채널을 저장할 배열을 생성
        left_channel = np.zeros(num_samples)
        right_channel = np.zeros(num_samples)

        # 각도를 라디안으로 변환
        theta = np.radians(azimuth_angle)

        # 각도에 따른 감쇠 계수를 계산
        attenuation = np.cos(theta)

        # 좌우 채널에 각각 감쇠 계수를 적용
        left_channel = self.audio_data * attenuation
        right_channel = self.audio_data * -attenuation

        return left_channel, right_channel

# 테스트 코드
if __name__ == "__main__":
    # SpatialAudio 클래스 객체 생성
    spatial_audio = SpatialAudio(num_channels=2)

    # 오디오 데이터 로딩
    spatial_audio.load_audio_data(audio_file="Audio_Samples\start-race-8-bit.mp3")
    
    # 2차원 패닝 적용
    left_channel, right_channel = spatial_audio.apply_2d_panning(azimuth_angle=30)
    # 패닝된 결과를 출력
    print("left_channel:", left_channel)
    print("right_channel:", right_channel)

    # 2차원 패닝 적용
    left_channel, right_channel = spatial_audio.apply_2d_panning(azimuth_angle=60)
    # 패닝된 결과를 출력
    print("left_channel:", left_channel)
    print("right_channel:", right_channel)

    # 2차원 패닝 적용
    left_channel, right_channel = spatial_audio.apply_2d_panning(azimuth_angle=90)
    # 패닝된 결과를 출력
    print("left_channel:", left_channel)
    print("right_channel:", right_channel)

    # 2차원 패닝 미적용
    left_channel, right_channel = spatial_audio.apply_2d_panning(azimuth_angle=0)
    # 패닝된 결과를 출력
    print("left_channel:", left_channel)
    print("right_channel:", right_channel)

    print ("left_channel:", spatial_audio.audio_data)