# parseltongue

### Challenge Text

>Author: @JohnHammond#6971
>
>Hisssss, can you ssssee ssssome sssssecretssss? 

### Challenge Work

We are given a file which turns out to be compile Python byte-code (`.pyc`).

```
parseltongue [master●●] % file parseltongue
parseltongue: python 3.8 byte-compiled
```

We find online that we can decompile python byte-code using pip modules, in this case `uncompyle6`.

```
parseltongue [master●●] % uncompyle6 parseltongue
```

We are then left with an unholy monstrosity of a script. After adding print statements to the bottom of the script to literally print out all variables defined, we get our flag.