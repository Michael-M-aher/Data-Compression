import json
import os
from pathlib import Path


class FloatingArithmetic:
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

    def _encode(self, text):
        self.range = [0, 1]
        self.encoded_text = ''
        prob = self._make_probability_dict(text)
        prob_ranges = self._make_probability_ranges_dict(prob)
        for i in text:
            self.range = self._getRange(prob_ranges[i])
        medFLoat = (self.range[0]+self.range[1])/2
        self.encoded_text = str(medFLoat)
        print(self.encoded_text)
        return self.encoded_text, prob_ranges

    def _get_symbol(self, prob_ranges, dec):
        for i in prob_ranges:
            if prob_ranges[i][0] <= dec <= prob_ranges[i][1]:
                return i

    def _get_code(self, dec):
        code = (dec-self.range[0])/(self.range[1]-self.range[0])
        return code

    def _decode(self, text, length, prob_ranges):
        self.range = [0, 1]
        self.decoded_text = ''
        for i in range(0, int(length)):
            dec = self._get_code(float(text))
            symb = self._get_symbol(prob_ranges, dec)
            self.decoded_text += symb
            self.range = self._getRange(prob_ranges[symb])
        return self.decoded_text

    def floating_arithmetic_compress(self):
        input_file = input("enter name of file to be compressed: ")
        filename, file_extension = os.path.splitext(input_file)
        with open(self.path / input_file, 'r') as file,  open(self.path / ('compressed_'+filename+'.txt'), 'w') as out_file:
            text = file.read()
            out, prob_ranges = self._encode(text)
            out_file.write(out+'|'+str(len(text))+'|')
            json.dump(prob_ranges, out_file)
        print("_________compressed successfully_________")

    def floating_arithmetic_decompress(self):
        input_file = input("enter name of file to be decompressed: ")
        with open(self.path / input_file, 'r') as file:
            r = file.read()
            decode = r.split('|')
            text = decode[0]
            length = decode[1]
            dict = decode[2]
            prob_ranges = json.loads(dict)
            decoded_text = self._decode(text, length, prob_ranges)
            with open(self.path / ('out.txt'), 'w') as output:
                output.write(decoded_text)
        print("_________decompressed successfully_________")


floatingArithmetic = FloatingArithmetic()
floatingArithmetic.floating_arithmetic_compress()
# floatingArithmetic.floating_arithmetic_decompress()
