# Bizarro

### Challenge Text

>This thing looks... bizarre? Can you find any secrets it may have? 
>Download the file below.

### Challenge Work

We are given a file named `bizarro` which is a zip file. Looking inside we can drill down to a diretory that *only* contains a `.bzr` directory. Taking a hint from the name of the challenge  and using `cat` on the `README` in `.bzr` we can dedude that this is a `Bazaar` challenge (https://bazaar.canonical.com/en/).

Looking in `bzr help` we can see that there are ways to view the logs. `bzr log -p` gives a bunch of information, showing the saving and creating of a ton of files. `bzr` also seems to have a `cat` command and the help page shows us we can view the contents of a file at a particular revision number.

Reading `bzr log -p` shows us that every other entry is the creation of a file, while the others are the deletion of that file. Since it is exactly every other one, we can just grab all of the filenames from `bzr log -p` and check the contents of all of them in their given revision number:

```
pwnbot :: b/bizzaro/bizarre % bzr log -p | grep added | awk '{print $4}' | tr "'" "\n" | grep  -v "^$" > filenames.txt
```

```python
import subprocess

file_names = open( "./filenames.txt", "r" ).readlines()

reversed_lines = file_names[::-1]

count = 1

for i in reversed_lines:
    print(subprocess.getoutput(f"bzr cat -r {count} {i}"))
    count += 2
```

After several iterations we get our flag:

> flag{is_bazaar_bizarre_or_is_it_just_me}