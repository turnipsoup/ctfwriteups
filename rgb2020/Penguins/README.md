# [Penguins](https://ctf.rgbsec.xyz/challenge?id=14) 

### Challenge Text

```
*waddle waddle*


~BobbaTea#6235, Klanec#3100
```

### Challenge Work

You are given a `.zip` file to unpack. Inside of it you see a few files and a `.git` directory. We can check which branches exist with `git branch`. After some looking in the git logs we see the name of a branch we do not see returned by the `git branch` command:

```
git [feature1] % cat .git/logs/head
[...]
27440c52e8a7a3d2e50f8fcdee0a88b0f937598d b474ae165218fec38ac9fb8d64f452c1270e68ea John Doe <John@doe.com> 1593465694 +0000	checkout: moving from master to b474ae1
b474ae165218fec38ac9fb8d64f452c1270e68ea b474ae165218fec38ac9fb8d64f452c1270e68ea John Doe <John@doe.com> 1593465718 +0000	checkout: moving from b474ae165218fec38ac9fb8d64f452c1270e68ea to fascinating
b474ae165218fec38ac9fb8d64f452c1270e68ea d14fcbfd3c916a512ad1b956cd19fb7be16c20c6 John Doe <John@doe.com> 1593465745 +0000	commit: an irrelevant file
d14fcbfd3c916a512ad1b956cd19fb7be16c20c6 cfd97cd36fe6c5e450d5057bf25aa1d7ddeca9ef John Doe <John@doe.com> 1593465781 +0000	commit: add content to irrelevant file
cfd97cd36fe6c5e450d5057bf25aa1d7ddeca9ef 5dcac0eddbcb4bffdec552a1172f84762a0b4174 John Doe <John@doe.com> 1593465822 +0000	commit: another perhaps relevant file
5dcac0eddbcb4bffdec552a1172f84762a0b4174 fb70ca39a7437eaba2850703018e1cf9073789e6 John Doe <John@doe.com> 1593465988 +0000	commit: probably not relevant
fb70ca39a7437eaba2850703018e1cf9073789e6 57adae71c223a465b6db3a710aab825883286214 John Doe <John@doe.com> 1593466025 +0000	commit: relevant file
[ommitted]
57adae71c223a465b6db3a710aab825883286214 800bcb90123137a6ee981c93c140bd04c75f507f John Doe <John@doe.com> 1593466646 +0000	commit: some things are not needed
[...]
```

Well, just because we cannot `checkout` the branch does not mean we cannot see what was in it:

```
logs [feature1] % git show 800bcb90123137a6ee981c93c140bd04c75f507f
```

```diff
commit 800bcb90123137a6ee981c93c140bd04c75f507f
Author: John Doe <John@doe.com>
Date:   Mon Jun 29 21:37:26 2020 +0000

    some things are not needed

diff --git a/perhaps_relevant b/perhaps_relevant
deleted file mode 100644
index 495f86b..0000000
--- a/perhaps_relevant
+++ /dev/null
@@ -1,2 +0,0 @@
-nope this aint relevant either chief
-
diff --git a/perhaps_relevant_v2 b/perhaps_relevant_v2
deleted file mode 100644
index ad12bc5..0000000
--- a/perhaps_relevant_v2
+++ /dev/null
@@ -1 +0,0 @@
-YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9
diff --git a/relevant b/relevant
deleted file mode 100644
index 222e0a5..0000000
--- a/relevant
+++ /dev/null
@@ -1,3 +0,0 @@
-haha
```

Thats interesting...

```
git [feature1] % echo "YXMgeW9kYSBvbmNlIHRvbGQgbWUgInJld2FyZCB5b3UgaSBtdXN0IgphbmQgdGhlbiBoZSBnYXZlIG1lIHRoaXMgLS0tLQpyZ2JjdGZ7ZDRuZ2wxbmdfYzBtbTE3c180cjNfdU5mMHI3dW40NzN9" | base64 -d
as yoda once told me "reward you i must"
and then he gave me this ----
rgbctf{d4ngl1ng_c0mm17s_4r3_uNf0r7un473}%
```

