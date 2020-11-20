# This software is distributed under the GNU Lesser General Public License.
 #  See the root of this repository for details.
 #  Copyright 2011, 2012 Daniel Powell 

from synthsound import *

out = initsynth()
sine_wave_1 = wavefunction(440, 9500, sin) # A pure 440 Hz (concert A4) tone.
sine_wave_2 = wavefunction(445, 9500, sin) # Very slightly sharp.

for i in xrange(1200):
	out.write(stereoframes(sine_wave_1, sine_wave_2, i*128)) # Interference beats are audible at a rate of 5 Hz

def square(x):
	# A square waveform.
	if x%TWO_PI < PI:
		return 1
	return -1

square_wave = wavefunction(440, 9500, square)
for i in xrange(1200):
	out.write(monoframes(swave, i*128)) # what a horrible sound
