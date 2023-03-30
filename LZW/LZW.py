from Tag import TagLZW


def lzw_compress():
    txt = input("Enter the text to be compressed: ")
    asciiDict = {chr(i): i for i in range(128)}
    pos = 127
    decodedtxt = [*txt]
    encodedtxt = []
    concatword = ''
    for i in range(0, len(decodedtxt)):
        if (concatword + decodedtxt[i] in asciiDict):
            concatword += decodedtxt[i]
        else:
            pos += 1
            asciiDict[concatword + decodedtxt[i]] = pos
            encodedtxt.append(
                TagLZW(asciiDict[concatword]))
            concatword = decodedtxt[i]

    if (concatword != ''):
        encodedtxt.append(TagLZW(asciiDict[concatword]))

    print(*encodedtxt, sep=" , ")


def lzw_decompress():
    txt = input("Enter the compressed text: ")
    asciiDict = {i: chr(i) for i in range(128)}
    curpos = 128
    encodedtxt = txt.split(' , ')
    decodedtxt = ''
    concatword = ''
    for i in range(0, len(encodedtxt)):
        pos = int(encodedtxt[i][1:-1])
        if (pos in asciiDict):
            decodedtxt += asciiDict[pos]
            if (concatword != ''):
                asciiDict[curpos] = concatword + asciiDict[pos][0]
                curpos += 1
            concatword = asciiDict[pos]
        else:
            decodedtxt += concatword + concatword[0]
            asciiDict[curpos] = concatword + concatword[0]
            curpos += 1
            concatword = asciiDict[pos]
    print(decodedtxt)


lzw_compress()
# ABAABABBAABAABAAAABABBBBBBBB
# <65> , <66> , <65> , <128> , <128> , <129> , <131> , <134> , <130> , <129> , <66> , <138> , <139> , <138>
