
from pyAudioAnalysis import audioBasicIO, audioSegmentation
import scipy.io.wavfile as wavfile
import numpy as np
from pydub import AudioSegment

def segment(path, file):
    Fs, x= audioBasicIO.read_audio_file( path + file)

    segments = audioSegmentation.silence_removal(x, Fs, 0.020, 0.020, smooth_window = 1.0, weight = 0.3, plot = False)
    print(segments)

    X= x[0:0]
    for i, segment in enumerate(segments):  
        print(i)
        t0= int(Fs * segment[0])
        t1= int(Fs * segment[1])
        # wavfile.write( path + 'segments/' + str(i)  + '.wav', Fs, x[t0:t1])
        X= np.concatenate( (X, x[t0:t1]),  axis=0)

    wavfile.write( path + 'seg_pyAudioAnalysis.wav', Fs, X )

path = 'data/'
file= 'full.wav'

segment(path, file)