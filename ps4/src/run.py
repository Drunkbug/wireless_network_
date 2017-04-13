import sys
import math
from random import randint
from scipy import special
import numpy


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

def generate_received_sequence(noise_sequence, th):
    """ generate received sequence by comparing with threshhold 

    Args:
        noise_sequence: An array represent the noise sequence
        th: A number represents the threshhold
    """
    return [ 1 if n > th else 0 for n in noise_sequence ]

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

def generate_sent_sequence(bit_rate, size):
    """ generate sent sequence
    Generates 10 million bits random 0s and 1s with given bit rate

    Args:
        size: A integer indicates how many bits are in the sequence
        bit_rate: A number represents bit rate 
    """
    sent_sequence = [numpy.random.choice(numpy.arange(0,2), p=[bit_rate, 1 - bit_rate]) for i in range(size)]
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

def main(snrs, bit_rate, th, size=1000000, mean=0):
    bers=[]
    bers2=[]
    # sent
    sent_sequence = generate_sent_sequence(bit_rate, size)
    signal_scheme = initialize_scheme(sent_sequence)
    for snr in snrs:
        # noise
        noise = generate_noise_array(mean, snr, size)
        noise_sequence = generate_noise_sequence(signal_scheme, noise) 
        # receive
        received_sequence = generate_received_sequence(noise_sequence, th)
        ber = get_bit_error_rate(sent_sequence, received_sequence, size)
        bers.append(ber)
        q = (1/2) * special.erfc((2 * snr)**(1/2) / (2**(1/2)))
        bers2.append(q)
    return snrs, bers, bers2

if __name__ == "__main__":
    # simulate channel under 0.5 bit rate
    print ("Simulating channel under 0.5 bit rate...")
    snrs = [3, 4, 5, 7,  9, 11]
    snrs, bers, bers2 = main(snrs, 0.5, 0)
    results = zip(snrs, bers, bers2)
    f = open("data_0_5.dat", "w")
    for r in results:
        print (str(r[0]) + " " + str(r[1]))
        f.write(str(r[0]) + " " + str('{:f}'.format(r[1])) + " " + str('{:f}'.format(r[2])) + "\n")
    f.close()
    print ("Output: data_0_5.dat")
    # simulate error rate under 0.01/0.99 bit rate for th=0
    print ("Simulating channel under 0.01 bit rate with threshhold 0...")
    snrs, bers, bers2 = main(snrs, 0.01, 0)
    results = zip(snrs, bers, bers2)
    f = open("data_0_01_th0.dat", "w")
    for r in results:
        print (str(r[0]) + " " + str(r[1]))
        f.write(str(r[0]) + " " + str('{:f}'.format(r[1])) + " " + str('{:f}'.format(r[2])) + "\n")
    f.close()
    print ("Output: data_0_01_th0.dat")

    # simulate error rate under 0.01/0.99 bit rate for th=0.3
    print ("Simulating channel under 0.01 bit rate with threshhold -0.2...")
    snrs, bers, bers2 = main(snrs, 0.01, -0.2)
    results = zip(snrs, bers, bers2)
    f = open("data_0_01_thn0_2.dat", "w")
    for r in results:
        print (str(r[0]) + " " + str(r[1]))
        f.write(str(r[0]) + " " + str('{:f}'.format(r[1])) + " " + str('{:f}'.format(r[2])) + "\n")
    f.close()
    print ("Output: data_0_01_thn0_2.dat")

    # simulate error rate under 0.01/0.99 bit rate for th=0.7
    print ("Simulating channel under 0.01 bit rate with threshhold 0.2...")
    snrs, bers, bers2 = main(snrs, 0.01, 0.2)
    results = zip(snrs, bers, bers2)
    f = open("data_0_01_th0_2.dat", "w")
    for r in results:
        print (str(r[0]) + " " + str(r[1]))
        f.write(str(r[0]) + " " + str('{:f}'.format(r[1])) + " " + str('{:f}'.format(r[2])) + "\n")
    f.close()
    print ("Output: data_0_01_th0_2.dat")
    print ("Simulation done.")

