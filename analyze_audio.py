import soundfile as sf
import librosa
import asyncio
from shazamio import Shazam, Serialize


async def query_shazam(song_file_path):
    shazam = Shazam()
    out = await shazam.recognize_song(song_file_path)
    print(out)

    serialized = Serialize.full_track(out)
    print(serialized)


def get_track_info(song_file_path):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(query_shazam(song_file_path))


def analyze_via_librosa(file):
    y, sr = librosa.load(f'{file}.wav', sr=None)
    print(y)
    print(sr)
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    print("tempo", tempo)
    print("beats", beats)


def analyze_via_soundfile(file):
    ob = sf.SoundFile(file)
    print('Sample rate: {}'.format(ob.samplerate))
    print('Channels: {}'.format(ob.channels))
    print('Subtype: {}'.format(ob.subtype))


if __name__ == "__main__":
    get_track_info('KUTX_1660754996.wav')
