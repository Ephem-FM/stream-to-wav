import time
from write_stream import write_stream_to_wav

import threading
import schedule


def run_threaded(station_name):
    job_thread = threading.Thread(
        target=write_stream_to_wav, args=(station_name,))
    job_thread.start()


if __name__ == "__main__":
    schedule.every(10).seconds.do(
        run_threaded, station_name='KUTX')
    while True:
        schedule.run_pending()
        time.sleep(1)
