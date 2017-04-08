import sys
import math
from random import randint
import numpy

#TODO in readme: pip install numpy, use python 3

def generate_noise_array(mean, snr):
    """ generate noise array based on gaussian noise form 

    Args:
        mean: An integer represents mean in pdf, 0 in zero mean noise voltage
        snr: A number represents Eb/N0
    """
    stddev = (1/(snr*2))**(1/2)
    noise = numpy.random.normal(mean, stddev, 1000000)
    return noise

def generate_noise_sequence(signal_scheme, noise):
    """ generate noise sequence 
    Add each noise sequence to the initial signal scheme

    Args: 
        signal_scheme: An array represent signal_scheme
        noise: An array represent corrsponding noise
    """
    return [ s + n for s, n in zip(signal_scheme, noise) ]

def generate_received_sequence(noise_sequence):
    """ generate received sequence by using optimal detection rule

    Args:
        noise_sequence: An array represent the noise sequence
    """
    return [ 1 if n > 0 else 0 for n in noise_sequence ]

def initialize_scheme():
    #TODO add bit rate
    """ initialize scheme with bit rate
    Generates 10 million bits random 0s and 1s with given bit rate
    Then map 0 to -1 and 1 to +1

    Args:
        bit_rate: A number represents bit rate 
    """
    # generate binary sequency with bit rate 1/2
    binary_sequence = [randint(0,1) for i in range(1000000)]
    # generate antipodal signaling shceme
    signal_scheme = [ (b - 1) if b == 0 else b for b in binary_sequence ]
    return signal_scheme


if __name__ == "__main__":

    signal_scheme = initialize_scheme()
    noise = generate_noise_array(0, 3)
    noise_sequence = generate_noise_sequence(signal_scheme, noise) 
    received_sequence = generate_received_sequence(noise_sequence)
    print (received_sequence)
    
