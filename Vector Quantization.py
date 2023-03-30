from PIL import Image
import numpy as np
import math


def distance(another, average):
    value = 0
    for i in range(len(average)):
        for j in range(len(average[0])):
            value += abs(average[i][j] - another[i][j])
    return value


def closer(n, values):
    c = distance(n, values[0])
    index = 0
    for i in range(1, len(values)):
        if c > distance(n, values[i]):
            c = distance(n, values[i])
            index = i
    return index


def associate(data, averages):
    sums = []
    counters = []
    l = [[0 for i in range(block_length)] for j in range(block_width)]
    for i in range(len(averages)):
        sums.append(l)
        counters.append(0)

    for i in range(len(data)):
        index = closer(data[i], averages)
        sums[index] = sums[index].plus(data[i])
        counters[index] += 1

    for i in range(len(averages)):
        averages[i] = sums[i].divide(counters[i])


def get_vector_average(block):
    sum_blocks = [[0 for i in range(block_length)] for j in range(block_width)]
    size_blocks = [[0 for i in range(block_length)]
                   for j in range(block_width)]
    avg_blocks = [[0 for i in range(block_length)] for j in range(block_width)]
    for block in blocks:
        for i in range(block_length):
            for j in range(block_width):
                sum_blocks[i][j] += block[i][j]
                size_blocks[i][j] += 1

    for i in range(block_length):
        for j in range(block_width):
            avg_blocks[i][j] = sum_blocks[i][j] / size_blocks[i][j]
    return avg_blocks


def floor(average):
    result = [[0 for i in range(block_length)] for j in range(block_width)]
    for i in range(len(average)):
        for j in range(len(average[0])):
            result[i][j] = math.floor(average[i][j])
    return result


def add(num, average):
    floor(average)
    result = [[0 for i in range(block_length)] for j in range(block_width)]
    for i in range(len(average)):
        for j in range(len(average[0])):
            average[i][j] = average[i][j] + num
    return result


def quantize(data, number_of_bits):
    avg = get_vector_average(data)
    values = [avg]
    while len(values) < number_of_bits:
        size = len(values)
        for j in range(size):
            current = values.pop(0)
            low = floor(current)
            high = add(1, low)
            values.append(low)
            values.append(high)
        associate(data, values)
    associate(data, values)
    return values


imgPath = 'image1.png'
img = Image.open(imgPath).convert("L")
print(type(img))
# converts image to numpy array
imgArr = np.asarray(img)
block_length = 3
block_width = 3
K = 16

blocks = []

# Divide the image into blocks
for i in range(0, imgArr.shape[0], block_length):
    for j in range(0, imgArr.shape[1], block_width):
        block = imgArr[i:i+block_length, j:j+block_width]
        blocks.append(block)

blocks = np.array(blocks)

codebook = quantize(blocks, K)
print(codebook)
# print(blocks[len(blocks)-1])

savePath = 'something.png'
decodedImg = Image.fromarray(imgArr)
decodedImg.save(savePath)  # will save it as gray image
