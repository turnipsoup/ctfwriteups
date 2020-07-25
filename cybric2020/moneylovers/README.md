# Moneylovers

### Challenge Text

> Author: Artur Khanov ([@awengar](https://t.me/awengar))
> We captured a transmission between a client and his bank. Help us hack it
> [**moneylovers.tar.gz**](https://cybrics.net/files/moneylovers.tar.gz)

### Challenge Work

Looking at the packet capture we see that this is a ton of TLSv1.2 connections, as if somebody is connecting to the same place over and over. Looking closely we do see it is reaching out to a public IP address.... `https://95.217.22.76/`

![webscreen](/Users/jeremy/Documents/notes/ctfs/cybric2020/moneylovers/webscreen.png)

Looking at the source code of this page we notice this odd bit:

```js
$(document).ready(function() {
	
    $("#kb").click(function(e){
		var mx = e.offsetX;
		var my = e.offsetY;
		$.ajax({
			type: "POST",
			url : "/key",
			data: JSON.stringify({x : mx, y: my}),
			contentType: "application/json",
			complete: function (a){
				if (a.responseJSON.status == "OK"){
					$("#pas").val(a.responseJSON.key);
				}
				if (a.responseJSON.status == "FLAG"){
					$("#bb2").hide();$("#pas").hide();$("#kb").hide();
					$("#getflag").css("display","block");
				}
			}
		});
		
	});
	$("#getflag").click(function(){
		$.ajax({
			type: "GET",
			url : "/getflag",
			complete: function (a){
				if (a.responseJSON.status == "OK"){
					$("#bb5").html(a.responseJSON.flag);
				}
				else{
					$("#bb5").html("Forbidden");
				}
			}
		});
	});
});
```

It seems that every single time we are pressing a button in the keypad a POST request is made to the server at the `/key` endpoint. Extrapolating from this, it seems our packet capture is an excrypted exchange of the key here in this manner.

After trying all sorts of stuff from Postman to `dirsearch` I finally decided to try entering a different protocol: `ftp://95.217.22.76/`:

```
Index of ftp://95.217.22.76/

Up to higher level directory
Name 	Size 	Last Modified
File:log.txt
	289 KB 	7/13/20 	9:25:00 AM PDT
```

Looking at log.txt, it appears to be a Master-Secret log, something that Wireshark explicitly accepts... We loaded this into Wireshark via `Preferences > TLS > (Pre)-Master-Secret log filename` and now we could see POST requests in plain text.

I exported the POST packets to JSON via Wireshark, and then extracted the click data:

```python
import json

json_file = json.loads(open("clicks.json","r").read())

for a in json_file:
    click_info = a["_source"]["layers"]["http"]["http.file_data"]
    print(click_info)
```

My teammate Unblvr then took this info and repeated the clicks to get the flag:

```python
from requests import session
import json

inputs = [
  {"x":383,"y":28},
  {"x":333,"y":101},
  {"x":113,"y":58},
  {"x":653,"y":50},
  {"x":588,"y":27},
  {"x":355,"y":141},
  {"x":385,"y":59},
  {"x":290,"y":185},
  {"x":111,"y":63},
  {"x":448,"y":20},
  {"x":141,"y":103},
  {"x":342,"y":105},
  {"x":92,"y":59},
  {"x":92,"y":59},
  {"x":168,"y":17},
  {"x":248,"y":179},
  {"x":206,"y":149},
  {"x":324,"y":13},
  {"x":421,"y":139},
  {"x":143,"y":106},
  {"x":639,"y":10},
  {"x":288,"y":100},
  {"x":318,"y":64},
  {"x":331,"y":186},
  {"x":409,"y":153},
  {"x":483,"y":110},
  {"x":43,"y":22},
  {"x":459,"y":57},
  {"x":108,"y":53},
  {"x":285,"y":104},
  {"x":248,"y":15},
  {"x":301,"y":185},
  {"x":648,"y":56},
  {"x":253,"y":27},
  {"x":258,"y":63},
  {"x":552,"y":108},
  {"x":106,"y":20},
  {"x":557,"y":145},
  {"x":584,"y":54}
]

s = session()
s.get("https://95.217.22.76/", verify=False)
URL = "https://95.217.22.76/key"
for inp in inputs:
    r = s.post(URL, json=inp, verify=False)
    print(r.text)

print(s.get("https://95.217.22.76/getflag", verify=False).text)

```

> cybrics{B4NK_S4V35_U_M0N3Y}