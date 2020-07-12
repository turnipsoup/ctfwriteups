# 

Hallo?

### Challenge Text

>The flag is exactly as decoded. No curly brackets.
>NOTE: keep the pound symbols as pound symbols!
>~BobbaTea#6235, Klanec#3100

### Challenge Work

Listening to the audio we can tell that these are DTMF tones being entered. Maybe we can decipher them a-la T9?

First let us get the DTMF tones from the file. Make sure to compare outputs from both of these commands from `dtmf.py`. (https://github.com/ribt/dtmf-decoder)

```
dtmf-decoder [master●] % ffmpeg -i down.mp3 down.wav
dtmf-decoder [master●] % ./dtmf.py -v ../down.wav
0:00 ....................
0:01 ................777.
0:02 ..7.7...777.........
0:03 ....................
0:04 ....................
0:05 .........44.........
0:06 ....................
0:07 ..............222..2
0:08 2...................
0:09 ....................
0:10 ....22...2222..22...
0:11 ....................
0:12 ............888.....
0:13 ....................
0:14 ..........33...333..
0:15 .33.................
0:16 ....................
dtmf-decoder [master●] % ./dtmf.py -v -t 10 ../down.wav
[... for brevity]
```

Once we are satisfied with what we believe the DTMF to be we can decode it:

```python
#!/usr/bin/env python3

str_one = "777 4 22 222 8 333 # 999 33 33 8 # 3 8 3 333 # 8 666 66 33 7777 #"

t9_text = {
    "2": "a",
    "22": "b",
    "222": "c",
    "3": "d",
    "33": "e",
    "333": "f",
    "4": "g",
    "44": "h",
    "444": "i",
    "5": "j",
    "55": "k",
    "555": "l",
    "6": "m",
    "66": "n",
    "666": "o",
    "7": "p",
    "77": "q",
    "777": "r",
    "7777": "s",
    "8": "t",
    "88": "u",
    "888": "v",
    "9": "w",
    "99": "x",
    "999": "y",
    "9999": "z"
}

def getsinglenumbergroup(num_message):
    char_str = num_message[0]
    for char in num_message[1:]:
        if char == char_str[-1]:
            char_str += char
        else:
            break
    return char_str

def getnumbergroups(num_message):
    number_groups = []
    while True:
        try:
            num_string = getsinglenumbergroup(num_message)
            number_groups.append(num_string)
            num_message = num_message[len(num_string):]
        except:
            break
    return number_groups

def numberstowords(num_str_list, t9_text):
    decoded_str = ""
    for number in num_str_list:
        try:
            decoded_str += t9_text[number]
        except:
            decoded_str += number
    return decoded_str

def getsentence(num_sentence):
    decoded_sentence = ""
    num_sentence = num_sentence.replace(".", "").replace(",", "").replace(":", "").replace("!","")
    for word in num_sentence.split(" "):
        word_groups = getnumbergroups(word)
        decoded_sentence += numberstowords(word_groups, t9_text)
        decoded_sentence += " "
    return decoded_sentence.upper()

print(getsentence(str_one))
print()

# R P H C T F # Y E U # D T D F # T F E E S #
#RGBCTF#YEE#DTMF#TONES# 
```

