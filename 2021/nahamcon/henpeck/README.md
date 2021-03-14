# henpeck

### Challenge Text

>Author: @JohnHammond#6971
>
>So I'll be honest, I never actually went through the Mavis Beacon program... 

### Challenge Work

We are given a `.pcap` file that contains a lot of USB info, so it is clear that this is a capture of a USB device. Reading the challenge we see that "Mavis Beacon" is mentioned, which is a typing program. We can assume that this is a packet capture of a USB keyboard, and I am assuming we need to find out what keys were typed.

I had recently watched a video on Youtube by Ben Eater about how keyboards work, so this was interesting. I then found the following script from a CTF in 2019: [https://blog.stayontarget.org/2019/03/decoding-mixed-case-usb-keystrokes-from.html](https://blog.stayontarget.org/2019/03/decoding-mixed-case-usb-keystrokes-from.html)


Per their instructions, we wanted to use `tshark` to extract the extra bits of information that tell us what actual bytes the keyboard sent over:

```
naham2021 % tshark -r henpeck.pcap -T fields -e usb.capdata | tr -d) :
```

This leaves us with a large file that has a tone of new lines, plus some data. We clean that up:

```python
stuff = [x.strip() for x in open('tshark.ext.txt', 'r').readlines() if x != '\n']

f = open("./tshark.new.txt", 'a')

for line in stuff:
    f.write(f"{line}\n")
```

Now we have what we want, except the top two lines of the file are much shorter than the others, so I manually deleted those.

We modify the script from the blog post by removing the `from future import ...` line, because we are using Python3 not Python2. When we run it against our new tsharked text file we get our flag:

```
naham2021 % python3 stolen_solve.py tshark.new.txt
sospacethespaceanswerspaceisspaceflag{f7733e0093b7d281dd0a30fcf34a9634}spacehahahahspacelolEnterc
```

The blog post goes into detail about how to interpret the byte sequences. Ben Eater does an amazing job in this video: [https://www.youtube.com/watch?v=7aXbh9VUB3U](https://www.youtube.com/watch?v=7aXbh9VUB3U))