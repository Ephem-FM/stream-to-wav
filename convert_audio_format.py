from pydub import AudioSegment
import os


def to_wav(file):
    src = f'{file}.mp3'
    dst = f'{file}.wav'

    # convert wav to mp3
    audSeg = AudioSegment.from_mp3(src)
    audSeg.export(dst, format="wav")

    # delete prior mp3 file
    mp3_path = f'{os.getcwd()}/{file}.mp3'
    if os.path.exists(mp3_path):
        os.remove(mp3_path)
        print(f'Deleted {mp3_path}.')
    else:
        print(f'{mp3_path} aint there boss.')
