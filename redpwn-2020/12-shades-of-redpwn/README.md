# 12-shades-of-redpwn

### Challenge Text

>Everyone's favorite guess god Tux just sent me a flag that he somehow encrypted with a color wheel! I don't even know where to start, the wheel looks more like a clock than a cipher... can you help me crack the code?

### Challenge Work

I know there is a way to crack this with `PIL` for Python, but I got fed up and tired so I just literally looked at the colors:

```python
# I got fed up and just looked at the colors
wheel_my_colors = {
    'gold': 1,
    'orange': 2,
    'red1': 3,
    'red2': 4, 
    'purple1': 5,
    'purple2': 6,
    'purple3': 7,
    'blue': 8,
    'seafoam': 9,
    'green': 10,
    'lime': 11,
    'yellow': 12
}

cipher_colors_found = [("blue", "purple2"), ("seafoam", "yellow"), ("blue", "gold"), ("blue", "purple3"), ("green", "red1"), ("red2", "seafoam"), ("seafoam", "seafoam"), ("red2", "red1"), ("seafoam", "purple3"), ("seafoam", "purple3"), ("red2", "gold"), ("seafoam", "orange"), ("red2", "seafoam"), ("purple3", "lime"), ("red2", "gold"), ("seafoam", "purple3"), ("purple3", "lime"), ("red2", "red2"), ("seafoam", "orange"), ("purple3", "lime"), ("red2", "red2"), ("seafoam", "purple2"), ("seafoam", "blue"), ("green", "purple1")]

cipher_colors_numbers = []

for pair in cipher_colors_found:
    cipher_colors_numbers.append((wheel_my_colors[pair[0]], wheel_my_colors[pair[1]]))

flag_string = ''
for ccn in cipher_colors_numbers:
    flag_string += chr((ccn[0] * 12 + ccn[1]))

print(flag_string)
```

```
PhillipJFryIV redpwn/12-shades » python3 solve.py
fxag{9u3ss1n9_1s_4n_4rt}
```

My math was off on the second pair, but it was an easy enough fix from x -> l

I may come back to this and resolve it in a more programmatic fashion.