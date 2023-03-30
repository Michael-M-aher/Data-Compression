# Data Compression

<img src="https://pbblogassets.s3.amazonaws.com/uploads/2018/09/20105751/data-compression.jpg" width="800" height="300">

## Brief

This project aims to provide an implementation of various data compression techniques in Python.<br>
The following compression techniques are implemented in this project:

- [LZ77 Compression](https://github.com/Michael-M-aher/Data-Compression/blob/main/LZ77%20Compression)
- [LZ78 Compression](https://github.com/Michael-M-aher/Data-Compression/blob/main/LZ78%20Compression)
- [LZW Compression](https://github.com/Michael-M-aher/Data-Compression/blob/main/LZW%20Compression)
- [Huffman Encoding](https://github.com/Michael-M-aher/Data-Compression/blob/main/Huffman%20Encoding)
- [Adaptive Huffman Encoding](https://github.com/Michael-M-aher/Data-Compression/blob/main/Adaptive%20Huffman%20Encoding)
- [Modified Huffman Encoding](https://github.com/Michael-M-aher/Data-Compression/blob/main/Modified%20Huffman%20Encoding)
- [Binary Arithmetic Coding](https://github.com/Michael-M-aher/Data-Compression/blob/main/Binary%20Arithmetic%20Coding)
- [Floating Arithmetic Coding](https://github.com/Michael-M-aher/Data-Compression/blob/main/Floating%20Arithmetic%20Coding)
- [Vector Quantization](https://github.com/Michael-M-aher/Data-Compression/blob/main/Vector%20Quantization)

## Installation

To use this project, you will need Python 3 installed on your system. You can download Python 3 from the official website: https://www.python.org/downloads/

Once you have Python 3 installed, you can use the algorithms.

## Usage

The project is divided into multiple modules, one for each compression technique. You can use these modules to compress and decompress data.

Here is an example of how to use the LZ77 module to compress a string:
```python
from lz77 import lz77_compress, lz77_decompress

text = "ABAABABAABBBBBBBBBBBBA"
window_size = 6
lookahead_buffer_size = 4

compressed_data = lz77_compress(text, window_size, lookahead_buffer_size)
print(compressed_data)
#output : <0, 0, 'A'> , <0, 0, 'B'> , <2, 1, 'A'> , <3, 2, 'B'> , <5, 3, 'B'> , <2, 2, 'B'> , <4, 4, 'B'> , <2, 2, 'A'>

original_text = lz77_decompress(compressed_data)
print(original_text)
#output : ABAABABAABBBBBBBBBBBBA
```
 

## Contributing
Pull requests are welcome. For major changes, please open an [issue](https://github.com/Michael-M-aher/Data-Compression/issues) first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Author

👤 **Michael Maher**

- Twitter: [@Michael___Maher](https://twitter.com/Michael___Maher)
- Github: [@Michael-M-aher](https://github.com/Michael-M-aher)

## Show your support

Please ⭐️ this repository if this project helped you!

<a href="https://www.buymeacoffee.com/michael.maher" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" height="60px" width="200" ></a>

## 📝 License

Copyright © 2022 [Michael Maher](https://github.com/Michael-M-aher).<br />
This project is [MIT](https://github.com/Michael-M-aher/Data-Compression/blob/main/LICENSE) licensed.
