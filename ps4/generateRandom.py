import sys
import math
from random import randint
import numpy

#TODO in readme: pip install numpy, use python 3

def generate_noise_array(mean, snr, size):
    """ generate noise array based on gaussian noise form 

    Args:
        mean: An integer represents mean in pdf, 0 in zero mean noise voltage
        snr: A number represents Eb/N0
    """
    stddev = (1/(snr*2))**(1/2)
    noise = numpy.random.normal(mean, stddev, size)
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

def get_bit_error_rate(sent_sequence, received_sequence, size):
    """ calculate bit error rate in the normal way

    Args:
        send_sequence: An arrary for the sequence number been sent
        received_sequence: An arrary for the sequence number been received
    """
    acc = 0
    for s, r in zip(sent_sequence, received_sequence):
        if s != r:
            acc += 1

    ber = acc / size
    return ber

def generate_sent_sequence(size):
    #TODO add bit rate
    """ generate sent sequence
    Generates 10 million bits random 0s and 1s with given bit rate

    Args:
        size: A integer indicates how many bits are in the sequence
        bit_rate: A number represents bit rate 
    """
    # generate binary sequency with bit rate 1/2
    sent_sequence = [randint(0,1) for i in range(size)]
    return sent_sequence


def initialize_scheme(sent_sequence):
    """ initialize scheme with bit rate
    Map 0 to -1 and 1 to +1

    Args:
        sent_sequence: An arrary represent the sent sequence
    """
    # generate antipodal signaling shceme
    signal_scheme = [ (b - 1) if b == 0 else b for b in sent_sequence]
    return signal_scheme


if __name__ == "__main__":
    # sent
    size = 1000000
    sent_sequence = generate_sent_sequence(size)
    signal_scheme = initialize_scheme(sent_sequence)
    # noise
    noise = generate_noise_array(0, 3, size)
    noise_sequence = generate_noise_sequence(signal_scheme, noise) 
    # receive
    received_sequence = generate_received_sequence(noise_sequence)
    ber = get_bit_error_rate(sent_sequence, received_sequence, size)
    
