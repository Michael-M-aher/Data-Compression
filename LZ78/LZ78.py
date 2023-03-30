from Tag import TagLZ78


def lz78_compress():
    txt = input("Enter the text to be compressed: ")
    dictionary = {}
    pos = 0
    decodedtxt = [*txt]
    encodedtxt = []
    concatword = ''
    for i in range(0, len(decodedtxt)):
        if (concatword + decodedtxt[i] in dictionary):
            concatword += decodedtxt[i]
        else:
            pos += 1
            dictionary[concatword + decodedtxt[i]] = pos
            if not (concatword in dictionary):
                encodedtxt.append(TagLZ78(0, decodedtxt[i]))
            else:
                encodedtxt.append(
                    TagLZ78(dictionary[concatword], decodedtxt[i]))
            concatword = ''

    if (concatword != ''):
        elempos = dictionary[concatword]
        encodedtxt.append(TagLZ78(elempos, 'null'))

    print(*encodedtxt, sep=" , ")


def lz78_decompress():
    txt = input("Enter the compressed text: ")
    dictionary = {}
    curpos = 1
    encodedtxt = txt.split(' , ')
    decodedtxt = ''
    for i in range(0, len(encodedtxt)):
        tag = encodedtxt[i].split('\'')
        pos = int(encodedtxt[i][1])
        symbol = tag[1]
        if (symbol == 'null'):
            symbol = ''
        if (pos == 0):
            totalsymbol = symbol
        else:
            totalsymbol = dictionary[pos] + symbol
        decodedtxt += totalsymbol
        dictionary[curpos] = totalsymbol
        curpos += 1
    print(decodedtxt)


lz78_compress()
# ABAABABAABABBBBBBBBBBA
