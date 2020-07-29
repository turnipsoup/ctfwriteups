### Challenge Text

```
This PNG looks to be valid, but when we open it up nothing loads. Any ideas?
```

### Challenge Work


**Note: I did not solve this challenge during the CTF, but my team did. I looked at other team's writeups for this.**

You start by running `file`, of course:

```
PhillipJFryIV ractf-2020/dimensionless_loading ‹master*› » file flag.png
flag.png: PNG image data, 0 x 0, 8-bit/color RGBA, non-interlaced
```

0x0?

When you look at the file in a hex editor like HexFiend you will see that the PNG header appears to be tampered with, as the width+height are zeroed:

```
89504E47 0D0A1A0A 0000000D 49484452 [[00000000 00000000]] 08060000 005B8AF0 30000020 00494441 54
```

We do notice that the crc32 checksum is intact: `5B8AF030`. We can calculate the width+height via brute force against this crc32 checksum.


### Lessons Learned

I had thought that just resizing the values of w+h to whatever I want, then calculating a new crc32 checksum would solve, but it did not. It would just open a large PNG that was just a black background.