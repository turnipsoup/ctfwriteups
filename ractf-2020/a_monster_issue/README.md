# A Monster Issue

### Challenge Text

```
Agent,

We've got a case of industrial espionage, quite an unusual one at that.
An international building contractor - Hamilton-Lowe, has written to us
that they are having their private client contracts leaked.

After conducting initial incident response, they managed to find a hidden
directory on one of their public facing web-servers. However, the strange
thing is, instead of having any sensitive documents, it was full of mp3 music
files.

This is a serious affair as Hamilton-Lowe constructs facilities for high-profile
clients such as the military, which means having building schematics leaked from
them could lead to a lapse in national security.

We have attached one of these mp3 files, can you examine it and see if there
is any hidden information inside?
```

### Challenge Work

*I am omitting the file due to the fact that it is obfuscated in a song that I do not have rights to reproduce.*

First thing we want to do in binwalk that file:

```
PhillipJFryIV ractf/monster » binwalk -e aero_chord.mp3                                127 ↵

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
1726          0x6BE           JPEG image data, JFIF standard 1.01
5162942       0x4EC7BE        Zip archive data, at least v2.0 to extract, uncompressed size: 191624, name: OwO.wav
5252619       0x50260B        End of Zip archive, footer length: 22
```

Unzipping the `.zip` and then playing OwO.wav produces clicking sounds that make you think something is hidden. Sure enough we see a hint when we look at the spectrogram: `Password{Shad0ws}`. 

We run binwalk on the new file:

```
PhillipJFryIV monster/_aero_chord.mp3.extracted » binwalk -e OwO.wav

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
179972        0x2BF04         Zip archive data, encrypted compressed size: 11480, uncompressed size: 11854, name: flag.png
191602        0x2EC72         End of Zip archive, footer length: 22
```

This `.zip` is not compatible witn `unzip` so we use `7za x file.zip`. It prompts us for a password, which we give, and now we can read our flag.

`ractf{M0nst3rcat_In5tin3t}`