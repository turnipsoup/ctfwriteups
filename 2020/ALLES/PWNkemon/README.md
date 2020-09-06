# PWNkemon

### Challenge Text

> The picture should explain everything.
> Careful, flag format is in a different format: `CSCG(...)`

### Challenge Work

First, lets unzip the challenge packet:

```bash
/tmp % unzip pwnkemon.zip
Archive:  pwnkemon.zip
  inflating: pwnkemon.jpg
  inflating: pwnkemon.logicdata
```

Second, lets look at the picture - 

![./pwnkemon.jpg](pwnkemon.jpg)

We see a logic analyzer attached to a GameBoy Link cable. We can see that the guide behind the Gameboys says Pokémon. We can probably assume we will be looking at a logic capture of a Pokémon trade.

We open the `.logicdata` file in the free demo of Saleae and we can confirm that it is a capture of four digital channels. We can also determine, from Google, that the Gameboy Link Cable uses SPI as a protocol. Saleae has a built in SPI decoder. After messsing with the settings we got some hexadecimal information to display.

Here is the SPI settings we used:

![](./saleae_settings.png)

We then went into Saleae and set a marker around where the file opened up naturally (around 92ms). We then enabled the SPI alayzer and then we saw things like this:

![](./saleae_bytes.png)

After this we exported the two channels to a CSV, keeping only the hexadecimal values. (See `spi.csv`)

We noticed these bytes did not decode into anything legible. At first we were stumped, then I had the thought to Google if the generation one Pokémon games used their own special encoding. It turns out they do. (You can read more [here](https://bulbapedia.bulbagarden.net/wiki/Character_encoding_in_Generation_I) if you are interested.)

![](./poke_chars.png)

For each byte that we get from the capture we take the first character and select that corresponding row, then we take the second character and select that corresponding column.

I took this chart and made it into a CSV of its own, replacing all of the `NULL` ,`Junk`, `Control`, or `Text box` characters with `*` . (See `gen_chars.csv`)

I then wrote a script to display the generated translations. I tried the MOSI first, but that was not right. Then I tried the MISO and that gave us our flag.

```python
import pandas as pd

chars_df = pd.read_csv("./gen_chars.csv")
spi_df = pd.read_csv("./spi.csv")

bytes_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}

def get_gen_char(byte_string):
    byte_one = byte_string[2]
    byte_two = byte_string[3]
    
    char_row = bytes_map[byte_one]
    
    return chars_df.iloc[char_row][byte_two].strip()
    
mosi_list = spi_df.MOSI.tolist()
miso_list = spi_df.MISO.tolist()

try_word = []

for char in miso_list:
    try:
        try_word.append(get_gen_char(char))
    except:
        pass
    
print("".join(try_word))
```

```
[..........]
CSCG(GONNA*-hack-em-A*ll-PWNkemo*n!!!)
[..........]
```

I removed the `*`'s from the string for the final true flag of: `CSCG(GONNA-hack-em-All-PWNkemon!!!)`

#### Bonus

Here is what the MISO and MOSI trade data looked like. Can you figure out which two they traded? [Here](https://docs.google.com/file/d/0B6wYRqisBsFfVkhBSmNlUEFVUEE/edit) is an example trade, showing the bytes. ([Here](http://www.adanscotney.com/2014/01/spoofing-pokemon-trades-with-stellaris.html) is the source.)

**MISO**

```
****AAAAAAAAAAAAA****************************************************8AAAAAAAAAAAAA************77777777y**p**x*’*777777777DRACON********I*qA9************ゥぉ*wiVkL'tSWSdVW*R********'s*****9*******9**;Zゥぉ*y*HKI'sHuHpHD*:********MN***C*YI*7*******C*ゥぉ**▶E*EaE*E*E*ぁ'r******7*b*X***.**3*****K:F*ゥぉ*y*H”ICI*H*Gs*⋯******3*[*U*▶**q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********DRACON*****DRACON*****DRACON*****DRACON*****RED*ASH*JACDRACON*****CSCG(GONNA*-hack-em-A*ll-PWNkemo*n!!!)******CHARMANDER*GOLDUCK****9]*7777********99*******************************************************************************************************************************************************************************************AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**********CCCCCCCCCCCCC**********CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC**********CCCCCCCCCCCCC************77777777*********E777777777DRACON*******I*qAf9*******9**;Zゥぉ*y*HKI'sHuHpHD*:********MN***C*YI*7*******C*ゥぉ**▶E*EaE*E*E*ぁ'r******7*b*X***.**3*****K:F*ゥぉ*y*H”ICI*H*Gs*⋯******3*[*U*▶**q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u*****************DRACON*****DRACON*****DRACON*****RED*ASH*JACDRACON*****RED*ASH*JAC-hack-em-A*ll-PWNkemo*n!!!)******CHARMANDER*GOLDUCK****RATTATA****9]*7777*******99********************************************************************************************************************************************************************************************ぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅ**********ぅぅぅぅぅぅぅぅぅぅぅぅぅ************77777777*▷'dL****zV777777777DRACON*******I*qAf9*******9**;Zゥぉ*y*HKI'sHuHpHD*:********MN***C*YI*7*******C*ゥぉ**▶E*EaE*E*E*ぁ'r******7*b*X***.**3*****K:F*ゥぉ*y*H”ICI*H*Gs*⋯******3*[*U*▶**q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u*****************DRACON*****DRACON*****DRACON*****RED*ASH*JACDRACON*****RED*ASH*JAC-hack-em-A*ll-PWNkemo*n!!!)******CHARMANDER*GOLDUCK****RATTATA****9]*7777*******99********************************************************************************************************************************************************************************************AAAAAAAAAAAAA**********CCCCCCCCCCCCC**********CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC**********CCCCCCCCCCCCC************77777777♂**W*y*MN**777777777DRACON******I*qAf*9I*7*******C*ゥぉ**▶E*EaE*E*E*ぁ'r******7*b*X***.**3*****K:F*ゥぉ*y*H”ICI*H*Gs*⋯******3*[*U*▶**q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u************************9****m*****?*k*4***ぃA****************DRACON*****DRACON*****RED*ASH*JACDRACON*****RED*ASH*JACRED*ASH*JACll-PWNkemo*n!!!)******CHARMANDER*GOLDUCK****RATTATA****PIDGEY*****9]*7777*******99********************************************************************************************************************************************************************************************AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**********CCCCCCCCCCCCC**********CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC**********CCCCCCCCCCCCC************77777777****Ae*.**777777777DRACON*******qAf**9**3*****K:F*ゥぉ*y*H”ICI*H*Gs*⋯******3*[*U*▶**q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u************************9****m*****?*k*4***ぃA**************************:*ゥぉ**▶H*I*HdV*I*************(****DRACON*****RED*ASH*JACDRACON*****RED*ASH*JACRED*ASH*JACDRACON*****n!!!)******CHARMANDER*GOLDUCK****RATTATA****PIDGEY*****MAGMAR*****9]*7777*******99********************************************************************************************************************************************************************************************AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA**********CCCCCCCCCCCCC**********CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC**********CCCCCCCCCCCCC************77777777I‘*GUew**0777777777DRACON******qAf**D9q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u************************9****m*****?*k*4***ぃA**************************:*ゥぉ**▶H*I*HdV*I*************(****D*******B*FVゥぉ*wiGSIぇF*V*V*Ag********▶******RED*ASH*JACDRACON*****RED*ASH*JACRED*ASH*JACDRACON*****DRACON*****CHARMANDER*GOLDUCK****RATTATA****PIDGEY*****MAGMAR*****MEWTWO*****9]*7777*******99********************************************************************************************************************************************************************************************ぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅぅ**********ぅぅぅぅぅぅぅぅぅぅぅぅぅ************77777777J*'l****O**777777777DRACON******qAf**D9q***********m*****r*****)**:O***************A*B****'t****ゥぉ*MB**********e******B********f******9**C*m***********C*u************************9****m*****?*k*4***ぃA**************************:*ゥぉ**▶H*I*HdV*I*************(****D*******B*FVゥぉ*wiGSIぇF*V*V*Ag********▶******RED*ASH*JACDRACON*****RED*ASH*JACRED*ASH*JACDRACON*****DRACON*****CHARMANDER*GOLDUCK****RATTATA****PIDGEY*****MAGMAR*****MEWTWO*****9]*7777*******99********************************************************************************************************************************************************************************************ぅぅぅぅぅぅぅぅぅぅぅぅぅぅ*********
```

**MOSI**

```
**88AAAAAAA‘AAAAA***********9*898.*****************8******8*********8A8*AA*AAAA‘AA**********77797779777**w*]*L*A**787778R*D*A*H*J*C*fe*D9A*f******9**C*m***********C*,**d*********************9****m*****?*k*8***ぃA************************v*ぃ*ゥぉ**▶”*I*ぇdVk***********A**(************B*FV4**wyHSIG*ァ*I**w******v*▶**********************************************************************************************RED*ASH*JACQE**ASH*IA*DRA*ON******ZAC*N***************************QAT)AT*‘***HID*EY**ぉ***AHM*Z*****M*(TW****‘************************Q**78777*******99********************************************************************************************************************************************************************************************9888889888889888*888888888*888889889889889889889889888888*88*88*89888888888888898888898998898898898898‘9AAAAAAAAA**********88CCCCDC“CC“DC“**********8889889889888889889889888*8888888889989C8C“DC“DCCC**********88C8C“CC“DCCCCC**********77777779777***”(t*5**7797779RED*A*H*J*C***D*9A********9****m*A***?*k*4****A*****************B*******'d**ゥ***▶h*I*HdV*I***P***⋯***PK*(*ァ**D***A***B*GVゥぉ*w.ぁTIぇ⋯*VY**A********A♂******S*******A**T4**wqIk*'tLWStVW*Z******u*'s*/***9****************************************************************************************R*D*A*H*J*CDR*CON*****BRACON*****DRACGO***************************PI*CEY‘***‘OAG*AR*A****GW*WP**A***(DG*GPN*A************************Q*797779*******q99*******************************************************************************************************************************************************************************************8*8888888989889889889888*88*8888988888889888889888*88*8888888889888889889888*8888888888889889889889889*89888*8888889889889888*8898888988889889888889888*888898888*889888889888888*88*8888888898889889889889*8888888888889889889889888988*8888888888889989888889*89*8888889888889888889889888*8889888889899889889888*888888888989988988988998888888888889889889889888*898888888988888988*889888*88*888888888888*889889888*8888889889889889889888888*8888888ぅ9ぅぅぅぅ♂ぇぅ**********98ぅ8ぅぅぅぅぅぅぅぅぅ**********98777977787y)‘*q*1**x8777777ZEDATHqNAC***DS9*************'l*****?*é*4***ぃ***************************:*▷ぉ*ぃ▼H*‘*Hd’*I****U***B***A[****D*v*****B**:ゥぉ*'tiG*Mぇ'm*M*V*Ag********▶***V**************ゥぉ*wiVoL't*XS**W*R***P****'s**A!*9A***************************************************************************************RE*AAS**IA*DQA*GN******ZAC*N*****D*ACO****************************PID*EY******AHM*Z**‘**M*(TW****A*CS*G(GOPNAぉ***********************Y*777777********99******************************************************************************************************************************************************************************************AAAA‘AA‘AA‘AA**********CCCDCCCBDCDC“**********888898888888888988988988888888889888888C8CCCCCC*CC**********89D8CCCCCD8“DC“**********77777779777**G*2kE**[7797779RED*ASH*J*C**D**9A***F*******▶*ゥぉ**▶H‘M*H/M*I:************)****DB******B[BVゥぉ*wi*(Iぇ'm*V***Ag****⋯**A7******************ゥ**w*:lL8ぃWS*:W********u*'t*****9***o***9**;Z.ぉ*2*HKI'sHu*pHD*[********MN***C*I****************************************************************************************DBACO******DRADONA****DR*CPNQ****DRA*ON***************************M*GOA******ME*)XO‘****CSC*:GO*NA*-hacé-em/A************************Q*777777*******E99*******************************************************************************************************************************************************************************************88888888988*889888*88*8889888889888*88*8888888889888*8888888889889889888*88888888898*9889888*8888889889A8A‘AAAA*AA**********8*“CCC*BCCBC“DC**********88*88*8888889889888888*888988988888988888C8C“DCCCCCC**********98C8C“CCCCCACCD**********77977797779***]'m****7877787RED**(H**AD****I9**D*******BぃHVゥぉ*wiぁTIぇ⋯*VY’*A********A♀******S*******A***4**w*:kL'tぅWStIW*R******u*'s*****9***O***9**;*▷ぉ*2*HKぉ'vHuぇpH-*[*****B**MN***C*YI*7*******C*ゥぉ**▶'r*GaE*G*E*ぇ'r******8*PK*X*)*.****************************************************************************************DRA*GP******ZAC*N*****D*ACO******DRADONI***************************GWT*O**‘**CCDG(GPNNA*-hqdk-uo-A*ll-PXN*amo************************I*777877********99********************************************************************************************************************************************************************************************888888988988988888898889889888888*89888898898888888888988988988888889889889888*8988889889889888*888888988988888A8AAAA‘AA‘A**********98“DC“*CCC“C“DC**********88*8889889889*8888889888888*888888988988C*C*BC“DC“D**********98C8*DC“DC““C8C**********79777977797'**ぃB****'s9777977ZGD*ATH*BAC***I*9**************ゥ**w2:kL8MWStIW*R******u*'s*****9***o***9**;*▼ぉ*2*HKI'vHuぇpH-*[*****B**MN***C*YI*7*******C*ゥぉ**▶E*GaE*G*E*ぇ'r******8*b*X*)*.**7*****K:H*ゥぉ*y*H’ICぉ*H*ぁt*⋯***U**3A[*U*♀******************************************************************************************DR*CPNQ****DRA*ON******RACOO*****DJACOF***************************ASCG[GONOA*/hacs-e▷/A**t-P*Nle*'t*n!-!)****************************Q**78777********99A******************************************************************************************************************************************************************************************9889888*8888889889889ぅ8*ぅぅpぅぅ8ぅぅA*********889Hぅ♂ぅぅぅぅぅ♂**********777797779771*******F*7778777RE**AS**JA****i*9**************♂ぉ*'tiVk*'vS*“dV**R*K***B**'s****A9*******9***;ゥぉ*y*!CI's!'lHp!”*:****V***MN*****YI*9******GA*ゥぉ**:・*E'・*E*・*ぁ'r******7Ab*XB**.**3******ぅF*4**y*H”.CI*H*Hs********3*]***▶******************************************************************************************D*ACON*****DRADO*ぉ****DR*CPNQ****DRA*ON***************************C*CH(*GNN**-h'sl-*m-A‘pl-*WNkuoo*▶!!!L**L**************************Q*777797********99*******************************************************************************************************************************************************************************************ぅ8ぅぅぅぅ♂ぅぅぅ**********
```

