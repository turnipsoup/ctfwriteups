# Thanks https://github.com/W3rni0/RACTF_2020#dimensionless-loading
# For the post-CTF writeup!
from zlib import crc32

data = open("flag.png",'rb').read()
index = 12

ihdr = bytearray(data[index:index+17])
width_index = 7
height_index = 11

for x in range(1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for i in range(len(height)):
            ihdr[height_index - i] = height[-i -1]
        for i in range(len(width)):
            ihdr[width_index - i] = width[-i -1]
        if hex(crc32(ihdr)) == '0x5b8af030':
            print("width: {} height: {}".format(width.hex(),height.hex()))
    for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]