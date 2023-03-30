from Tag import TagLZ77


def find_match(text, window_size, lookahead_size, i):
    window_start = max(0, i - window_size)
    window_end = i
    lookahead_start = i
    best_match = None
    for j in range(window_start, window_end):
        if text[j] == text[lookahead_start]:
            matchcnt = 1
            for k in range(1, lookahead_size):
                if j + k >= window_end or text[j + k] != text[lookahead_start + k]:
                    break
                matchcnt += 1
            match = (lookahead_start - j, matchcnt,
                     text[lookahead_start + matchcnt])
            if not best_match or match[1] >= best_match[1]:
                best_match = match
    return best_match


def lz77_compress():
    text = input("Enter the text to be compressed: ")
    window_size = int(input("Enter the window size: "))
    lookahead_size = int(input("Enter the lookahead size: "))
    compressed = []
    i = 0
    while i < len(text):
        match = find_match(text, window_size, lookahead_size, i)
        if match:
            compressed.append(TagLZ77(match[0], match[1], match[2]))
            i += match[1]
        else:
            compressed.append(TagLZ77(0, 0, text[i]))
        i += 1
    return compressed


def lz77_decompress():
    compressed = input("Enter the compressed text: ")
    encodedtxt = compressed.split(' , ')
    decodedtxt = ''
    for i in range(0, len(encodedtxt)):
        tag = encodedtxt[i][1:-1].split(',')
        pos = int(tag[0].trim())
        size = int(tag[1].trim())
        symbol = tag[2].trim()
        for j in range(0, size):
            decodedtxt += decodedtxt[-pos + j]
        decodedtxt += symbol
    return decodedtxt


text = 'ABAABABAABBBBBBBBBBBBA'
text2 = "<0, 0, 'A'> , <0, 0, 'B'> , <2, 1, 'A'> , <3, 2, 'B'> , <5, 3, 'B'> , <2, 2, 'B'> , <5, 5, 'B'> , <1, 1, 'A'>"
compressed = lz77_compress()
# decompressed = lz77_decompress()
print(*compressed, sep=" , ")
# print(decompressed)
