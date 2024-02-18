import numpy as np
from scipy.signal import find_peaks
import soundfile as sf
import matplotlib.pyplot as plt
import librosa


counter = 0

def tap_audio(indata, frames, time, status):

    signal = np.reshape(indata, indata.size)

    rxx = np.abs(np.correlate(sig, sig,mode='full'))





def simple_vad(sig, connection,  frame_len, counter):
    # print('simple_vad:before reshape sig = ', sig.shape)
    sig = np.reshape(sig, sig.size)
    # print('simple_vad: after reshaping sig = ', sig.shape)
    rxx = np.abs(np.correlate(sig,sig,mode='full'))    
    ths = np.std(rxx)
    peaks,_ = find_peaks(rxx, threshold=0.25*ths,width=3)
    # peaks = len(peaks)
    # Pavan added the below line. commenting to test if just len(peaks) will make the fan run more frequentlu
    #peaks = round(len(peaks)*rxx[len(sig)-1])
    peaks = round(len(peaks))

    # global i
    global peaks_avg
    # global FRAME_LEN
    
    peaks_avg.append(peaks)
    counter += 1

    # def scale_values(pass_list):
    #     scaled_list=[]
    #     for i in pass_list:
    #         i=i/10
    #         i=

    print(f'frame len = {FRAME_LEN}')
    if  len(peaks_avg) == FRAME_LEN :
        val = np.mean(peaks_avg)

        val = (val/10)
        #val= 100/(1+np.exp(-val/30))
        val = np.log10(val+10)*62

        # val = np.tanh(val/50)*100 # Did not get the fan to move fast enough. Also stopped the fan
        val_new = val if 0 < val < 100 else 99
        print(f"!PEAKS! pavan code -- peaks-{peaks}, peaks_avg {np.mean(peaks_avg)}, val{val}, val_new{val_new}, i{i}")
        print("Array = ", peaks_avg)
        peaks_avg = [val_new, peaks]
        i = 0

        # map 0-640 to 30-70


        sending_data(str(int(np.round(peaks))), connection)
    
   
    #return (rxx,peaks)