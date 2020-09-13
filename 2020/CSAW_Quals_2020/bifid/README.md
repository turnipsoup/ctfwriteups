# Difib

### Challenge Text

> Welcome to crypto. We start with the classics! Deliver the decrypted form of the message to the guard on your journey. 
> `nc crypto.chal.csaw.io 5004`

### Challenge Work

When you connect to the service, you are greeted with someone asking you to pass a message from the "boss":

```
difib % nc crypto.chal.csaw.io 5004
> Alright messenger, what did the boss tell you to tell me? Better be right or you're not getting in!

Sounds bogus! Scram, you're not getting in!
```

Due to the name of the challenge, and based on the contents of the files, we can guess that this is a [Bifid Cipher](https://en.wikipedia.org/wiki/Bifid_cipher). The challenge also came with a few hints, as so few people had solved this challenge by the time we did (we got the third solve):

>1) We only want perfect ramblings!!
>2) NEAR perfect ramblings? it seems our cipher is a little off...
>3) Length of keys is 25, which (cleaned-up) ramblings would fit that?

So lets clean up the ramblings like they suggest:

```python
import string

ramblings = [x.strip() for x in open("/Users/jeremy/code/ctfs/csaw/difib/ramblings", "r").readlines()]
ct = open("/Users/jeremy/code/ctfs/csaw/difib/message", "r").read().strip()

alphabet = "zyxwvutsrqponmlkjihgfedcba"

################################################################################
def clean_ramble(ramble):
    return ramble.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
################################################################################

clean_rambles = [clean_ramble(x) for x in ramblings]
```

We ran through a bunch of these keys until we felt like we were going in circles. One of our teammates asked for a hint from one of the admins, and we got this:

> try using multiple keys in a certain order

We tried iterating through the keys in the order they appeared, but that did not help. After that I recalled that one of my teammates, Someone, pointed out that the name of the challenge was a hint - "difib", which is Bifid backwards.

```python
from pycipher import Bifid

################################################################################
def debifid(key, ct, period):
    return Bifid(key, period).decipher(ct)
################################################################################

current_ct = ct
    
for ramble in clean_rambles[::-1]:
    if len(ramble) < 27:
        current_ct = debifid(ramble.replace("j",""), current_ct, 5)
        print(current_ct.lower())
```

The final text returned from this script is what we need to modify and pass to the service.

```
difib % ./ramble.py
vqpuoifwvtzswgewymbyifovtdbcccszziqixzbmowezhmrheohhuiwqhpoitqctrstkfrywzdowimrunqwxssdppeyigmtaissebinrsywvhlosmz
zducogufdywwrlzwfwuoiufdocqcfcumyyvkqwnwpuzgcnfuhikmiprucimosttdbumqtgzqyhywigtpmpsdxuneqpwsgticdhqucigtnvrxhvnrup
sxdwofzyulriqorwukvrpgyugcettcyucmukprqwobopdvahvihumcoipmwoxoqmeyymbrdaewyrypkfvnynxiycstryxuhbqdwknqpfgmiexsvswx
dgdmekktnmfmumiatqvrysuanowevwniqsorbmdcoxuucxolbhmmgvpqnnvpvhfeumbyqhewwisomyqmsrnthgpygorypixgggfsplqknpoipsdcei
dwiienvnwoyhmlrahtnoygstntdvwdsnaborpdxvxexgnxiqbdydvpithnrrfrtvyybbqwdumvfxbfdmnqnbkgglbmrlmalgzacabedctppoeapvgr
dnwtznuigomaheyhwpdowghsnokdtixxnifdgaqrxyddnnmqtiyfcninefeohpraobpbuwknvyyolwuanuqzxhxpxmkfmklatqrawzcdefzhvxfizf
dyopzpqtxymhedyiaweowyfsemtgwkxmbqnlelthwqhsfqoohpasfmbnmenghhqxtbzpbwlwomtmtkdcqptbniixnmdckqqagrrqcawrxdocuekoax
clphfuogdwpqxgwiwbzweemwfliwbqemuzdlytomhevbeicsxfbgsqffplvxtixiqbkzoyylhwkuqxroqrpfxgegxhrmrhkrqqmrctrixclkwbkaox
bdhoeswxxiplvdixvwdcebwymwfxqwpkccueoyfthtpbagnbntkwirtochlpuyiqiclytrkxwfhuhnnodntopgrpbgrxkmszfavnynzyukdwfbyrnb
brdyaqgwkxpwlzxxqeowxamtfwqwvxqoquzghfhzhtrldvgnbuqbrpurzaqhiicniypuhhqbgdrumzrekheirvnrfsttgqsamrgzzeguzqbszryntr
dhuvepfkshfdgdxnzqfczngqbwmfihqtuitkvhxtgxfusowkrytqcguoonvhpxqndybibstpdggrmmunaahzmraltstoqrhgfmsrzrcigiimgrnmzt
vdfzttphyxfkdvxowmhbmeotxufayhvfpltxvbiegigahehtfysvvnmnefohwwirdiebaxtvuuvmlmyacszsfalrpbwbeobgihxrcfavmgugsrhwak
daxdktqffcfdosxkwhrlismyzgqfvhbcpdkbevcxgolwumlrqdntvctsaiikwwrrylwlyxtutrnmqyolcmsbfrplfacavflufewrayoxhgksnswgah
btaxyxiqkcorhzfgfonlboyarmevuwiuobpiknaquvwxlrgblrvitdnynvxioqoakldpabtbrhtkkautwlmkxuyfwdpiqtngiwmaazxcwgeuoswaue
fgruawmhwrkzulagxfrlfdnyxknigwiwqykavnalqzxswqmbycyehxtvumpzovtckkdfeqrpdftnaoaaxckgmtzwqdqaaxtbxsvysqxzwgxidryghq
acudrcwzfakkldbgwbuavcdhtiiqzzzxdenvsakotrmwgocmfxxhclhpmykztqhknzzeafdsfacomasouxwumqbzwdochohysuxstvqwgxwyglyhbw
wczdpzdawikubkdyewwsyzzwtqizizzrealvnkzlwxmgrmbitmxwohzbeoaydenvonmihvamsimfkfdlulxdwzxumzhbndhxrunstxxqqyttweehmm
tgcwvayuwzbkkgdfcffrecxyziqimzzmhzlarnekrqapmevnzsophszbolevnrymbnylopouezsfgdnlugydxxeosntkdvkxgtxbwfxqxecwetemtb
lgxskacyzxincfnffkhrxuywxiqawzizwypdndbkalqpaexxqnkcswwlnnniygazocuollnyxcedaewqxkesyuleuntekafetxwbwiqdxxenwsxewo
xustxsomexunnecessaryxtextxthatxholdsxabsolutelyxnoxmeaningxwhatsoeverxandxbearsxnoxsignificancextoxyouxinxanyxway
```

```
difib % nc crypto.chal.csaw.io 5004
> Alright messenger, what did the boss tell you to tell me? Better be right or you're not getting in!
just some unnecessary text that holds absolutely no meaning whatsoever and bears no significance to you in any way

flag{t0ld_y4_1t_w4s_3z}
```

### Further Thoughts

Looking back: this challenge should have noted that you needed multiple keys to get through, without an admin hint. Releasing hints on the challenge itself throughout the CTF is fine and normal. However - nasking the admins personally for a hint and then finding out you needed multiple keys seems "guessy" at best. If they had included this in one of the dropped hints on the challenge I would not have thought twice about it.