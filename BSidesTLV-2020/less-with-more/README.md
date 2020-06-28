# More With Less

### Challenge Text

>You need some EFF in your life.
>http://bsidesctf.s3-website.eu-central-1.amazonaws.com/MoreWithLess.E01

### Challenge Work

You are given no hints and a `.E01` Expert Witness (EnCase 6) file. So let us recover files with `ewftools`:

```
pwnbot :: ctfs/bsides/mwl % tsk_recover -e MoreWithLess.E01 recovered

pwnbot :: ctfs/bsides/mwl % ll recovered                                                                                                                130 ↵
total 1.4G
drwxrwxr-x.  4 galleywest galleywest 4.0K Jun 28 17:49 '$Extend'
drwxrwxr-x.  4 galleywest galleywest 4.0K Jun 28 17:49 '$Recycle.Bin'
-rw-rw-r--.  1 galleywest galleywest 1.4G Jun 28 17:49  pagefile.sys
drwxrwxr-x. 11 galleywest galleywest 4.0K Jun 28 17:50  ProgramData
drwxrwxr-x. 21 galleywest galleywest 4.0K Jun 28 17:49 'Program Files'
drwxrwxr-x. 16 galleywest galleywest 4.0K Jun 28 17:49 'Program Files (x86)'
drwxrwxr-x. 10 galleywest galleywest 4.0K Jun 28 17:50  Python38
-rw-rw-r--.  1 galleywest galleywest  16M Jun 28 17:50  swapfile.sys
drwxrwxr-x.  2 galleywest galleywest 4.0K Jun 28 17:50 'System Volume Information'
drwxrwxr-x.  5 galleywest galleywest 4.0K Jun 28 17:50  Users
drwxrwxr-x. 69 galleywest galleywest 4.0K Jun 28 17:53  Windows
```

First we notice there is a User named after the CTF...this is likely where we should look first. Digging around in here we notice that the History file for Google Chrome is present, and it is a SQLIte database:

```
pwnbot :: ctfs/bsides/mwl % ll recovered/Users
total 16K
drwxrwxr-x. 17 galleywest galleywest 4.0K Jun 28 17:50 bsidestlv2020
drwxrwxr-x.  3 galleywest galleywest 4.0K Jun 28 17:50 Default
-rw-rw-r--.  1 galleywest galleywest  174 Jun 28 17:50 desktop.ini
drwxrwxr-x. 10 galleywest galleywest 4.0K Jun 28 17:50 Public

pwnbot :: ctfs/bsides/mwl % file recovered/Users/bsidestlv2020/AppData/Local/Google/Chrome/User\ Data/Default/History
recovered/Users/bsidestlv2020/AppData/Local/Google/Chrome/User Data/Default/History: SQLite 3.x database, last written using SQLite version 3031001
```

Well, lets see what they searched for...

![flag_find.png](flag_find.png 'flag-find.png')

```
BSIDESTLV2020{HideYourNeedleInTheHayStack}
```

