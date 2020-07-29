# Schwifty Mind!


### Challenge Text
> Let's send a message to aliens 🛸❤️😊
>
>Peace among worlds!

### Challenge Work

My teammate Stamparm solved this one, but I did a write up so I could make sure I was able to do this in the future.

When we look at the PCAP we can see that there are a ton of SSH connections being made on 127.0.0.1. If you look at all of the conversation in Wireshark...

![wirehshark](conversations.png)

We can see that the length of total Packets from A -> B for each conversation seems to only be of two values....binary?


```python
import pandas as pd
df = pd.read_csv("pcap.csv")
```


```python
bin_valuesA = df["Packets A → B"].values

bin_string1 = ""
bin_string2 = ""

# Lets try both options at once here to save time
for i in bin_valuesA:
    if i > 40:
        bin_string1 += "0"
        bin_string2 += "1"
    if i < 40:
        bin_string1 += "1"
        bin_string2 += "0"
```


```python
def splitbinstring(bin_string):
    chunks, chunk_size = len(bin_string), len(bin_string)//28
    return [ bin_string[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

# Thanks! https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def bitstostring(b=None):
    str_array = []
    for x in b:
        str_array.append(chr(int(x, 2)))
    return "".join(str_array)
```


```python
for target in [bin_string1, bin_string2]:
    print(bitstostring(splitbinstring(target)))
```

    ¾¬¶¬ÌÊ Ì ¬ÜÎÈ ËÎ±Þ
    ASIS{l3t5_g3t_S#hvv1f7y_4ga1N!}

