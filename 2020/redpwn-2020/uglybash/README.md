# uglybash

### Challenge Text

> This bash script evaluates to `echo dont just run it, dummy \# flag{...}` where the flag is in the comments.
>
> The comment won't be visible if you just execute the script. How can  you mess with bash to get the value right before it executes?
>
> Enjoy the intro misc chal.

### Challenge Work

You can run this script with the `-x` command and send this output to a text file:

```
pwnbot :: ctfs/redpwn/uglybash % bash -x cmd.sh &> cmd.txt
```

Open this file with `less` and search for the `printf` strings. Go down far enough and you will see it:

```
+++ printf %s '#'
[...]
+++ printf %s ' '
[...]
+++ printf %s f
[...]
+++ printf %s l
[...]
+++ printf %s a
[...]
+++ printf %s g
[...]
+++ printf %s '{'
[...keep going...]
```

`flag{us3_zsh,_dummy}`

I actually got first blood on this one :)