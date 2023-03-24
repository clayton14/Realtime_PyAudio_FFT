from src.stream_analyzer import Stream_Analyzer
import time
import numpy as np
"""
get frequencies from FFT

if volume of frequency reaches a min value genrate color


"""



ear = Stream_Analyzer(
                device = 12,        # Pyaudio (portaudio) device index, defaults to first mic input
                rate   = None,               # Audio samplerate, None uses the default source settings
                FFT_window_size_ms  = 60,    # Window size used for the FFT transform
                updates_per_second  = 1000,  # How often to read the audio stream for new data
                smoothing_length_ms = 50,    # Apply some temporal smoothing to reduce noisy features
                n_frequency_bins = 400, # The FFT features are grouped in bins
                visualize = 1,               # Visualize the FFT features with PyGame
                verbose   = False,    # Print running statistics (latency, fps, ...)
                height    = 450,     # Height, in pixels, of the visualizer window,
                window_ratio = 2.6666666666666665  # Float ratio of the visualizer window. e.g. 24/9
            )


# raw_fftx, raw_fft, binned_fftx, binned_fft = ear.get_audio_features()
# print(f"LOW:{raw_fft[:300]}, MID:{raw_fft[300:]}")


def freq_to_hsv(data, brightness):
    return (max(0, min(data, 360)), brightness)


def freq_to_rgb(data):
    return(max(0, min(data, 255)), max(0, min(data, 255)), max(0, min(data, 255)))


fps = 60  #How often to update the FFT features + display
last_update = time.time()
while True:
    if (time.time() - last_update) > (1./fps):
        last_update = time.time()
        raw_fftx, raw_fft, binned_fftx, binned_fft = ear.get_audio_features()
        ear.equalizer_strength = .5
        #print(freq_to_hsv(ear.strongest_frequency ,100))
        print(freq_to_rgb(ear.strongest_frequency))
    elif True:
        time.sleep(abs(((1./fps)-(time.time()-last_update)) * 0.99))




# get volume of audio live in db
def volume(data):
    pass



    