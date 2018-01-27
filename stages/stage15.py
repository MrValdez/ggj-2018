# Find the strongest signal

import math
import pygame
from .stage import Stage, Text, Projectile, Collidable, Avatar

import pyaudio
import struct
import math

class ClapChecker:
    def get_rms(self, block):
        # RMS amplitude is defined as the square root of the 
        # mean over time of the square of the amplitude.
        # so we need to convert this string of bytes into 
        # a string of 16-bit samples...

        # we will get one short out for each 
        # two chars in the string.
        count = len(block)/2
        format = "%dh"%(count)
        shorts = struct.unpack( format, block )

        # iterate over the block.
        sum_squares = 0.0
        for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
            n = sample * self.SHORT_NORMALIZE
            sum_squares += n*n

        return math.sqrt( sum_squares / count )

    def __init__(self):
        INITIAL_TAP_THRESHOLD = 0.010
        FORMAT = pyaudio.paInt16 
        self.SHORT_NORMALIZE = (1.0/32768.0)
        CHANNELS = 2
        RATE = 44100  
        INPUT_BLOCK_TIME = 0.05
        self.INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)

        self.OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    

        self.UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME # if we get this many quiet blocks in a row, decrease the threshold

        self.MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME # if the noise was longer than this many blocks, it's not a 'tap'

        pa = pyaudio.PyAudio()                                 #]
                                                               #|
        self.stream = pa.open(format = FORMAT,                      #|
                 channels = CHANNELS,                          #|---- You always use this in pyaudio...
                 rate = RATE,                                  #|
                 input = True,                                 #|
                 frames_per_buffer = self.INPUT_FRAMES_PER_BLOCK)   #]

        self.tap_threshold = INITIAL_TAP_THRESHOLD                  #]
        self.noisycount = self.MAX_TAP_BLOCKS+1                          #|---- Variables for noise detector...
        self.quietcount = 0                                         #|
        self.errorcount = 0                                         #]         

    def update(self):
        try:                                                    #]
            block = self.stream.read(self.INPUT_FRAMES_PER_BLOCK)         #|
        except IOError as e:                                      #|---- just in case there is an error!
            self.errorcount += 1                                     #|
            print( "(%d) Error recording: %s"%(errorcount,e) )  #|
            self.noisycount = 1                                      #]

        amplitude = self.get_rms(block)
        if amplitude > self.tap_threshold: # if its to loud...
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > self.OVERSENSITIVE:
                self.tap_threshold *= 1.1 # turn down the sensitivity

        else: # if its to quiet...
            if 1 <= self.noisycount <= self.MAX_TAP_BLOCKS:
                print("CLAP")
                return amplitude / self.tap_threshold
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > self.UNDERSENSITIVE:
                self.tap_threshold *= 0.9 # turn up the sensitivity
        return 0


class Stage15(Stage):
    def __init__(self, resolution):
        super().__init__(resolution)
        self.texts = [Text("Clap to transmit a BIT of noise", (255, 255, 255), self._center_text)]

        try:
            self.clapChecker = ClapChecker()
        except:
            self.clapChecker = None
            print("Clap checker code failed. skipping this stage")
            
        self.reset()
        
    def reset(self):
        self.delta = 0
        self.claps_remaining = 13

    def update(self, input, tick):
        if self.claps_remaining <= 0:
            return True
            
        if self.clapChecker is None:
            return True
        
        if input.button:
            print("making noise with button")
            self.claps_remaining -= 1

        try:
            delta = self.clapChecker.update()
            if delta:
                self.claps_remaining -= 1
                self.delta = delta
        except:
            print("microphone unreliable. skipping stage")
            return True

    def draw(self, screen):
        r, g, b = [128 * self.delta, 128 * self.delta, 198 * self.delta]
        screen.fill([min(r, 255), min(g, 255), min(b, 255)])
        super().draw(screen)