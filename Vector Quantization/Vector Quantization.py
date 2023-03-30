import numpy as np
import os
from PIL import Image
from pathlib import Path
from MyList import MyList


class Vector_Quantization:
    def __init__(self, photo_length, photo_width, block_size, book_size):
        self.path = Path(os.path.dirname(os.path.realpath(__file__)))
        self.photo_length = photo_length
        self.photo_width = photo_width
        self.block_size = block_size
        self.book_size = book_size

    def _divide_blocks(self, imgArr):
        blocks = []
        for i in range(0, imgArr.shape[0], self.block_size):
            for j in range(0, imgArr.shape[1], self.block_size):
                block = imgArr[i:i+self.block_size, j:j+self.block_size]
                blocks.append(block)

        blocks = np.array(blocks)
        return blocks

    def _get_vector_average(self, data):
        size = len(data[0])
        avg = MyList(size)
        for i in range(len(data)):
            for r in range(size):
                for c in range(size):
                    avg.average[r][c] += data[i][r][c]
        return avg.divide(len(data))

    def _closer(self, n, values):
        c = values[0].distance(n)
        index = 0
        for i in range(1, len(values)):
            if c > values[i].distance(n):
                c = values[i].distance(n)
                index = i
        return index

    def _associate(self, data, averages):
        sums = [MyList(len(data[0])) for _ in range(len(averages))]
        counters = [0 for _ in range(len(averages))]

        for i in range(len(data)):
            index = self._closer(data[i], averages)
            sums[index] = sums[index].plus(data[i])
            counters[index] += 1

        for i in range(len(averages)):
            averages[i] = sums[i].divide(counters[i])

    def _quantize(self, data):
        avg = self._get_vector_average(data)
        values = [avg]
        while len(values) < self.book_size:
            size = len(values)
            for j in range(size):
                current = values.pop(0)
                low = current.floor()
                high = low.add(1)
                values.append(low)
                values.append(high)
            self._associate(data, values)
        self._associate(data, values)
        return values

    def _encode(self, blocks, codeBook):
        encoded = []
        for i in range(len(blocks)):
            index = self._closer(blocks[i], codeBook)
            encoded.append(codeBook[index])
        return np.array(encoded)

    def _decode(self, encoded):
        decoded = np.empty((self.photo_length, self.photo_width))
        block_idx = 0
        for i in range(0, self.photo_length, self.block_size):
            for j in range(0, self.photo_width, self.block_size):
                decoded[i:i+self.block_size, j:j +
                        self.block_size] = encoded[block_idx].average
                block_idx += 1
        return decoded

    def vector_quantize(self, imgArr):
        blocks = self._divide_blocks(imgArr)
        codeBook = self._quantize(blocks)
        encoded = self._encode(blocks, codeBook)
        decoded = self._decode(encoded)
        return decoded


def main():
    project_path = Path(os.path.dirname(
        os.path.realpath(__file__)))
    iamge_name = input('enter image name: ')
    imgPath = str(project_path) + '/' + iamge_name
    img = Image.open(imgPath).convert("L")
    # converts image to numpy array
    imgArr = np.asarray(img)
    block_size = int(input('Enter Block Size: '))
    K = int(input('Enter Book Size: '))
    vq = Vector_Quantization(imgArr.shape[0], imgArr.shape[1], block_size, K)
    decoded = vq.vector_quantize(imgArr)
    decoded_img = Image.fromarray(decoded)
    decoded_img.convert('RGB').save('compressed.png')
    decoded_img.show()


main()
