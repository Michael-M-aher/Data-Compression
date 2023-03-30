import json
import math
import os
from pathlib import Path


class BinaryArithmetic:
    def __init__(self):
        self.path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.range = [0, 1]
        self.encoded_text = ''
        self.decoded_text = ''

    def _make_frequency_dict(self, text):
        freq = {}
        for char in text:
            if (char not in freq):
                freq[char] = 0
            freq[char] += 1
        return freq

    def _make_probability_dict(self, text):
        freq = self._make_frequency_dict(text)
        prob = {}
        for key in freq:
            prob[key] = freq[key] / sum(freq.values())
        return prob

    def _make_probability_ranges_dict(self, prob):
        sortednames = sorted(prob.keys())
        prob_ranges = {}
        start = 0
        for key in sortednames:
            prob_ranges[key] = [start, start + prob[key]]
            start += prob[key]
        return prob_ranges

    def _getRange(self, i):
        return [self.range[0] + (self.range[1] - self.range[0]) *
                i[0], self.range[0] + (self.range[1] - self.range[0]) * i[1]]

    def _rangeScale(self):
        while (self.range[0] > 0.5 or self.range[1] < 0.5):
            if (self.range[0] > 0.5):
                self.range[0] = 2*(self.range[0]-0.5)
                self.range[1] = 2*(self.range[1]-0.5)
                self.encoded_text += '1'
            if (self.range[1] < 0.5):
                self.range[0] = 2*self.range[0]
                self.range[1] = 2*self.range[1]
                self.encoded_text += '0'

    def _encode(self, text):
        self.range = [0, 1]
        self.encoded_text = ''
        prob = self._make_probability_dict(text)
        prob_ranges = self._make_probability_ranges_dict(prob)
        for i in text:
            self.range = self._getRange(prob_ranges[i])
            self._rangeScale()
        self.encoded_text += '1'
        k = self._get_k_value(prob_ranges)
        self.encoded_text += '0' * (k-1)
        return self.encoded_text, prob_ranges

    def _get_k_value(self, prob_ranges):
        mn = 9999999.0
        k = 0
        for i in prob_ranges:
            temp = (prob_ranges[i][1] - prob_ranges[i][0])
            if temp < mn:
                mn = temp
        k = math.log((1/mn), 2)
        k = math.ceil(k)
        return k

    def _getDeciaml(self, text, k):
        dec = int(text, 2)/(2**k)
        return dec

    def _get_symbol(self, prob_ranges, dec):
        for i in prob_ranges:
            if prob_ranges[i][0] <= dec <= prob_ranges[i][1]:
                return i

    def _get_code(self, dec):
        code = (dec-self.range[0])/(self.range[1]-self.range[0])
        return code

    def _decode(self, text, prob_ranges):
        self.range = [0, 1]
        self.encoded_text = ''
        self.decoded_text = ''
        k = self._get_k_value(prob_ranges)
        i = 0
        tmp = text[i: i+k]
        dec = self._getDeciaml(tmp, k)
        while (i+k < len(text)):
            print(dec)
            symbol = self._get_symbol(prob_ranges, dec)
            self.decoded_text += symbol
            print(self.decoded_text)
            self.range = self._getRange(prob_ranges[symbol])
            print(self.range)
            self._rangeScale()
            print(self.range)
            if (self.encoded_text != ''):
                i += len(self.encoded_text)
                tmp = text[i: i+k]
                dec = self._getDeciaml(tmp, k)
                print('shif', dec)
                self.encoded_text = ''
            print('b', dec)
            dec = self._get_code(dec)
            print('a', dec)

        self.decoded_text += self._get_symbol(prob_ranges, dec)
        return self.decoded_text

    def binary_arithmetic_compress(self):
        input_file = input("enter name of file to be compressed: ")
        filename, file_extension = os.path.splitext(input_file)
        with open(self.path / input_file, 'r') as file,  open(self.path / ('compressed_'+filename+'.txt'), 'w') as out_file:
            text = file.read()
            out, prob_ranges = self._encode(text)
            out_file.write(out+'|')
            json.dump(prob_ranges, out_file)
        print("_________compressed successfully_________")

    def binary_arithmetic_decompress(self):
        input_file = input("enter name of file to be decompressed: ")
        with open(self.path / input_file, 'r') as file:
            r = file.read()
            decode = r.split('|')
            text = decode[0]
            dict = decode[1]
            prob_ranges = json.loads(dict)
            print(self._get_k_value(prob_ranges))
            decoded_text = self._decode(text, prob_ranges)
            with open(self.path / ('out.txt'), 'w') as output:
                output.write(decoded_text)
        print("_________decompressed successfully_________")


binaryArithmetic = BinaryArithmetic()
# binaryArithmetic.binary_arithmetic_compress()
binaryArithmetic.binary_arithmetic_decompress()
