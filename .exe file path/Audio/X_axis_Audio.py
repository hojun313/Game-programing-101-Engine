import pygame

def play_audio_with_stereo(audio_file_path, x_axis_value, screen_width=1920):
    # Initialize pygame
    pygame.init()
    pygame.mixer.init()

    # Load audio file
    audio = pygame.mixer.Sound(audio_file_path)

    # Calculate pan value
    pan = x_axis_value / screen_width

    channel = pygame.mixer.Channel(0)
    channel.set_volume(1 - pan, pan)

    # Play audio
    channel.play(audio)

if __name__ == "__main__":
    play_audio_with_stereo(audio_file_path="Audio_Samples\ding.mp3", x_axis_value=100)
    
    # Wait until audio is finished
    while pygame.mixer.get_busy():
        pass
    
    play_audio_with_stereo(audio_file_path="Audio_Samples\ding.mp3", x_axis_value=1500)
    
    # Wait until audio is finished
    while pygame.mixer.get_busy():
        pass

    pygame.quit()