import multiprocessing
import requests
import time
import schedule

import convert_audio_format

stations = {
    'DDR': 'https://dublindigitalradio.out.airtime.pro/dublindigitalradio_a',
    'KUTX': 'https://kut.streamguys1.com/kutx-web'
}


def write_stream_to_wav(station_name):
    file_name = f'{station_name}_{str(int(time.time()))}'
    p = multiprocessing.Process(
        target=stream_to_mp3, name="Write Stream to MP3", args=(stations[station_name], file_name))
    p.start()
    time.sleep(10)
    p.terminate()
    convert_audio_format.to_wav(file_name)


def stream_to_mp3(station_url, file_name):
    with requests.get(station_url, stream=True) as r:
        with open(f'{file_name}.mp3', 'wb') as f:
            try:
                for block in r.iter_content(1024):
                    f.write(block)
            except KeyboardInterrupt:
                f.close()
