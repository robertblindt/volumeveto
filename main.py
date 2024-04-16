# Does Loudness Measurements
import pyloudnorm as pyln
# Converts Wav to Pandas for pyloudnorm
import soundfile as sf
# Technically dont need this.  Just for listenback...
from pydub.playback import play

import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import rfft, fft, ifft



def audio_metering(main_wav_file):
    # section_width in seconds
    # Convert main audio to get gain adjustment
    main_data, main_rate = sf.read(main_wav_file)
    print(main_rate, len(main_data))
    # Create Meter
    meter = pyln.Meter(main_rate)

    # find full clip audio loudness
    full_clip_loudness = meter.integrated_loudness(main_data)
    count = 0
    one_second_ave_loudness = []
    # There should be overlap when going point to point, but for first pass inspection, I am just doing full window jumps. 
    for i in range(int(len(main_data)/main_rate)):
        count+=1
        one_second_loudness = meter.integrated_loudness(main_data[i*main_rate:(i+1)*main_rate])

        # Moved over to a Jupyter Notebook to fix the FFT issues
        # X = rfft(main_data[i*main_rate:(i+1)*main_rate])
        # N = len(X)
        # n = np.arange(N)

        # T = N/main_rate
        # freq = n/T 
        # print(freq, n, T)
        # plt.figure(figsize = (12, 6))
        # plt.plot(freq, np.abs(X), 'r')
        # plt.subplot(121)

        # plt.stem(freq, np.abs(X), 'b', \
        #         markerfmt=" ", basefmt="-b")
        # plt.xlabel('Freq (Hz)')
        # plt.ylabel('FFT Amplitude |X(freq)|')
        # plt.show()

        one_second_ave_loudness.append(one_second_loudness)
    return full_clip_loudness, one_second_ave_loudness


# audio_metering('thecount.wav')

audio_metering('youtube_snippet.wav')

# audio_metering('twitch_cheer.wav')
