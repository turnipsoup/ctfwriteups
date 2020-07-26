# Google Cloud

### Challenge Text

>                    Author: Vlad Roskov ([@mrvos](https://t.me/mrvos))                
>                    I am storing some important stuff in Google's cloud.
>                    Nooo no no, not on Google's disks — in the cloud itself.
>                    [**gcloud.tar.gz**](https://cybrics.net/files/gcloud.tar.gz)

### Challenege Work

When you first open the pcap file you notice that it is entirely ICMP messages. Looking at the data presented in Wireshark we could see some strings being echoed that talked about `pingfs`. So I looked into it: https://github.com/yarrick/pingfs. Because ICMP requires that the data sent to the server be echoed back to the sender you can technically store data over ICMP.

I used Wireshark to export the entire pcap as a JSON file and set about extracting any binary data that may have been sent over:

```python
import json
import binascii

json_file = json.loads(open("./packets.json", "r").read())

def clean_data(data):
    return data.replace(":","").upper()

text_list = []
data_list = []

for a in json_file:
    icmp_info = a["_source"]["layers"]["icmp"]
    raw_data_payload = clean_data(icmp_info["data"]["data.data"])
    payload_bytes = bytearray.fromhex(raw_data_payload)

    try:
        text_list.append(payload_bytes.decode())
    except:
        data_list.append(binascii.hexlify(payload_bytes))

print(f"data_list set is {len(set(data_list))} long")    

for i in data_list:
    with open("out.bin", "ab") as f:
        f.write(i)
```

```shell
google % cat out.bin| xxd -p -r > file.bin
google % binwalk file.bin

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
10315         0x284B          JPEG image data, EXIF standard
10327         0x2857          TIFF image data, little-endian offset of first image directory: 8
20344         0x4F78          JPEG image data, EXIF standard
20356         0x4F84          TIFF image data, little-endian offset of first image directory: 8
26794         0x68AA          JPEG image data, EXIF standard
26806         0x68B6          TIFF image data, little-endian offset of first image directory: 8

[...]
```

We can see a ton of JPEG images ([or at least headers](https://github.com/corkami/pics/blob/master/binary/JPG.png)). If you scroll down in your hex editor you will see that the JPEGs are getting longer. Scrolling to the bottom and copying from the last JPEG header down give us our file.

![flag](https://raw.githubusercontent.com/turnipsoup/ctfwriteups/master/cybric2020/google-cloud/flag.jpg)

