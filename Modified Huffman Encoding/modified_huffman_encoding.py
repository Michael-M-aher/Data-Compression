from pathlib import Path
import os
import json
import heapq
from Tree_Node import TreeNode


class HuffmanCoding:
    def __init__(self):
        self.path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.heap = []
        self.codebook = {}
        self.decodebook = {}

    def _make_frequency_dict(self, text):
        freq = {}
        delkeys = []
        for char in text:
            if (char not in freq):
                freq[char] = 0
            freq[char] += 1
        freq['others'] = 0
        for key in freq:
            # probality of others
            prob = 0.03
            if (freq[key]/len(text) <= prob):
                freq['others'] += 1
                delkeys.append(key)
        for i in delkeys:
            del freq[i]
        return freq

    def _make_heap(self, frequency):
        for key in frequency:
            node = TreeNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def _merge_nodes(self):
        while (len(self.heap) > 1):
            lft = heapq.heappop(self.heap)
            rht = heapq.heappop(self.heap)

            node = TreeNode(None, lft.freq+rht.freq)
            node.left = lft
            node.right = rht
            heapq.heappush(self.heap, node)

    def _create_code_helper(self, node, node_code):
        if (node == None):
            return
        if (node.char != None):
            self.codebook[node.char] = node_code
            self.decodebook[node_code] = node.char
            return

        self._create_code_helper(node.left, node_code + '0')
        self._create_code_helper(node.right, node_code + '1')

    def _create_codebook(self):
        root = self.heap[0]
        self._create_code_helper(root, '')

    def _get_encoded_text(self, text):
        encoded_text = ''
        for char in text:
            if (char not in self.codebook and 'others' in self.codebook):
                encoded_text += self.codebook['others'] + \
                    format(ord(char), '08b')
            else:
                encoded_text += self.codebook[char]
        self.decodebook['len'] = len(encoded_text)
        return encoded_text

    def _get_byte_array(self, encoded_text):
        leftover = len(encoded_text) % 8
        if (leftover != 0):
            encoded_text += '0' * (8 - leftover)
        byte_array = bytearray()
        for i in range(0, len(encoded_text), 8):
            byte = encoded_text[i:i+8]
            byte_array.append(int(byte, 2))
        return byte_array

    def _get_bit_string(self, byte_array):
        bit_string = ""
        for byte in byte_array:
            bit_string += format(byte, '08b')
        return bit_string[0:(self.decodebook['len'])]

    def _encode_file(self, text, file_extension):
        freq = self._make_frequency_dict(text)
        self._make_heap(freq)
        self._merge_nodes()
        self._create_codebook()
        self.decodebook['ext'] = file_extension
        encoded_text = self._get_encoded_text(text)
        byte_array = self._get_byte_array(encoded_text)
        decodebook = self.decodebook
        return byte_array, decodebook

    def _decode_file(self, decodebook, byte_array):
        self.decodebook = decodebook
        data = self._get_bit_string(byte_array)
        decoded_text = ''
        concat_code = ''
        i = 0
        while i < len(data):
            concat_code += data[i]
            if (concat_code in self.decodebook):
                if (self.decodebook[concat_code] == 'others'):
                    charAsci = int(data[i+1:i+9], 2)
                    decoded_text += chr(charAsci)
                    i += 8
                else:
                    decoded_text += self.decodebook[concat_code]
                concat_code = ''
            i += 1
        return decoded_text

    def hauffman_compress(self):
        input_file = input("enter name of file to be compressed: ")
        filename, file_extension = os.path.splitext(input_file)
        with open(self.path / input_file, 'r') as file,  open(self.path / ('compressed_'+filename+'.bin'), 'wb') as binary_file, open(self.path / ('dict_' + filename), 'w') as decode:
            text = file.read()
            byte_array, decodebook = self._encode_file(text, file_extension)
            binary_file.write(bytes(byte_array))
            json.dump(decodebook, decode)
        print("_________compressed successfully_________")

    def hauffman_decompress(self):
        input_file = input("enter name of file to be decompressed: ")
        filename = os.path.splitext(input_file)[0][11:]
        with open(self.path / input_file, 'rb') as binary_file, open(self.path / ('dict_' + filename), 'r') as decode:
            decodebook = json.load(decode)
            decoded_text = self._decode_file(
                decodebook, binary_file.read())
            with open(self.path / ('out' + decodebook['ext']), 'w') as output:
                output.write(decoded_text)
        print("_________decompressed successfully_________")


h = HuffmanCoding()
h.hauffman_compress()
# h.hauffman_decompress()
