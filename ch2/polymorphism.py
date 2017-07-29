#! used to demonstrate polymorphism.

class AudioFile:
    def __init__(self, filename):
        if filename.endswith(self.ext):
            raise Exception('Invalid file format')
        self.filename = filename

class MP3File(Audiofile):
    ext = 'mp3'
    def play(self):
        print(f'Playing {self.filename} as mp3')

class WavFile(Audiofile):
    ext = 'wav'
    def play(self):
        print(f'Playing {self.filename} as wav')

class OggFile(Audiofile):
    ext = 'ogg'
    def play(self):
        print(f'Playing {self.filename} as ogg')
