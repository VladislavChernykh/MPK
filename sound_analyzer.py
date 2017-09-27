from __future__ import print_function, division

import thinkdsp
import thinkplot

import numpy
import wave

wave = cos_sig.make_wave(duration=0.5, framerate=11025)
spectrum = wave.make_spectrum()
spectrum.plot()
thinkplot.config(xlabel='frequency (Hz)', legend=False)
saw_sig = thinkdsp.SawtoothSignal(freq=440)
saw_sig.plot()
saw_wave = saw_sig.make_wave(duration=0.5)
saw_wave.make_audio()
saw_wave.make_spectrum().plot()