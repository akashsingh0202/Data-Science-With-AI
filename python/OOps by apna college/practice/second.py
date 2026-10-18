class Camera:
    def take_photo(self):
        print("Photo clicked")

class MusicPlayer:
    def play_music(self):
        print("Music playing")

class Smartphone(Camera, MusicPlayer):
    pass

phone = Smartphone()
phone.take_photo()
phone.play_music()