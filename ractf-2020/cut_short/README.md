# Cut Short

First, we look at the image presented to us:

```
PhillipJFryIV ractf/cut_short » file flag.png
flag.png: data
```

We notice its is not recognizable. Let us open both this file and a valid `.png` with a hex editor, like HexFiend.

Doing so we can see that `00000000 49454E44 AE426082` is at the end of the valid file, but is right after the PNG magic bytes (`89 50 4E 47 0D 0A 1A 0A`) at the start of this file. Cutting `00000000 49454E44 AE426082` from its current location and appending it to the end of the file allows us to open the new `.png` file and read our flag.

`ractf{1m4ge_t4mp3r1ng_ftw}`