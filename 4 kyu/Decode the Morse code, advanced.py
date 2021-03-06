# In this kata you have to write a Morse code decoder for wired electrical telegraph.
# Electric telegraph is operated on a 2-wire line with a key that, when pressed, connects the wires together, which can
# be detected on a remote station. The Morse code encodes every character being transmitted as a sequence of "dots"
# (short presses on the key) and "dashes" (long presses on the key).
#
# When transmitting the Morse code, the international standard specifies that:
#
# "Dot" – is 1 time unit long.
# "Dash" – is 3 time units long.
# Pause between dots and dashes in a character – is 1 time unit long.
# Pause between characters inside a word – is 3 time units long.
# Pause between words – is 7 time units long.
# However, the standard does not specify how long that "time unit" is. And in fact different operators would transmit at
# different speed. An amateur person may need a few seconds to transmit a single character, a skilled professional can
# transmit 60 words per minute, and robotic transmitters may go way faster.
#
# For this kata we assume the message receiving is performed automatically by the hardware that checks the line
# periodically, and if the line is connected (the key at the remote station is down), 1 is recorded, and if the line is
# not connected (remote key is up), 0 is recorded. After the message is fully received, it gets to you for decoding as a
# string containing only symbols 0 and 1.
#
# For example, the message HEY JUDE, that is ···· · −·−−   ·−−− ··− −·· · may be received as follows:
#
# 1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011
#
# As you may see, this transmission is perfectly accurate according to the standard, and the hardware sampled the line
# exactly two times per "dot".
#
# That said, your task is to implement two functions:
#
# Function decodeBits(bits), that should find out the transmission rate of the message, correctly decode the message to
# dots ., dashes - and spaces (one between characters, three between words) and return those as a string. Note that some
# extra 0's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have
# trouble discerning if the particular sequence of 1's is a dot or a dash, assume it's a dot.
# 2. Function decodeMorse(morseCode), that would take the output of the previous function and return a human-readable
# string.
#
# NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.
#
# The Morse code table is preloaded for you (see the solution setup, to get its identifier in your language).
#
#
# Eg:
#   morseCodes(".--") //to access the morse translation of ".--"
# All the test strings would be valid to the point that they could be reliably decoded as described above, so you may
# skip checking for errors and exceptions, just do your best in figuring out what the message is!
#
# Good luck!

MORSE_CODE = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h',
              '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p',
              '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x',
              '-.--': 'y', '--..': 'z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}

spam = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'

bacon = '00011100010101010001000000011101110101110001010111000101000111010111010001110101110000000111010101000101110100011101110111000101110111000111010000000101011101000111011101110001110101011100000001011101110111000101011100011101110001011101110100010101000000011101110111000101010111000100010111010000000111000101010100010000000101110101000101110001110111010100011101011101110000000111010100011101110111000111011101000'

egg = '- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.'

ham = '1'

long_spam = '111111000000111111000000111111000000111111000000000000000000111111000000000000000000111111111111111111000000111111000000111111111111111111000000111111111111111111000000000000000000000000000000000000000000111111000000111111111111111111000000111111111111111111000000111111111111111111000000000000000000111111000000111111000000111111111111111111000000000000000000111111111111111111000000111111000000111111000000000000000000111111'


def decode_morse(morse_code):
    return ' '.join(''.join([MORSE_CODE.get(n) for n in x.split(' ')]) for x in morse_code.strip().split('   '))


# "Dot" – is 1 time unit long.
# "Dash" – is 3 time units long.
# Pause between dots and dashes in a character – is 1 time unit long.
# Pause between characters inside a word – is 3 time units long.
# Pause between words – is 7 time units long.


def decode_bits(bits):
    import re
    bits = bits.strip('0')
    sequence = re.compile('(1+)(0*)(1*)')
    match_object = sequence.search(bits)
    if len(match_object.group(1)) == 1:
        bit_rate = 1
    elif len(bits) % len(match_object.group(1)) == 0:
        bit_rate = len(match_object.group(1))
    elif len(match_object.group(1)) == 3 and len(bits) % 3 != 0:
        bit_rate = 1
    elif len(match_object.group(1)) % 3 == 0:
        bit_rate = int(len(match_object.group(1)) / 3)
    bits = ''.join([bits[index] for index in range(0, len(bits), bit_rate)])
    bits = bits.replace('0000000', '   ').replace('000', ' ').replace('111', '-').replace('1', '.').replace('0', '')
    return decode_morse(bits)



