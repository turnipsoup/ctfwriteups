# Peculiar Packet Capture

### Challenge Text

```
Agent,

We have a situation brewing. Last week there was an attack on the prime minister
of Morocco. His motorcade was stopped by a road blockade where heavily armed men
opened fire on them. Fortunately, the prime minister was able to escape safely but
many personnel and a few other ministers did not.

ATLAS, a multi-national Private Military Corporation (PMC) based in Colorado, USA,
is our main suspect. We believe they were hired to conduct the hit by the opposition
political party.

We flew Agent Jason to Colorado to investigate further. He gained access to their
building's reception area dressed in a suit acting as a potential client with an
appointment. He was able to intercept wireless network traffic from their corporate
wireless network before being escorted out by guards when they realised the bluff.

The network capture is attached below, see if you can recover any important documents
which could help us tie ATLAS to the Morocco incident.
```

### Challenge Work

First we open the thing up in Wireshark. We notice a total of three devices. Here we will nickname them: `Zte`, `Gemtek`, `Azurewav`. Looking at the first packet it is a beacon packet from `Zte`. So `Zte` is a router of some kind. `Gemtek` then authenticates to `Zte`. `Gemtek` then starts a conversation with `Azurewav`. 

Looking at the conversation between `Gemtek` and `Azurewav` we can determine that `Zte` is just a wireless device betwixt them:

```
BSS Id: Zte_c0:59:b3 (c0:fd:84:c0:59:b3)
```

Looking at the EAPOL packets we realize this is WPA with a password. Let us use `aircrack-ng`:

```
galleywest:ppc/ $ aircrack-ng -z -w /usr/share/wordlists/rockyou.txt ATLAS_Capture.pcap

[00:00:06] 25625/14344392 keys tested (4290.17 k/s)

      Time left: 55 minutes, 37 seconds                          0.18%

                           KEY FOUND! [ nighthawk ]

      Master Key     : 2B C3 90 3F 5A 04 8E BF 0B 35 06 13 B3 73 E5 32
                       11 C0 A7 F4 99 F3 42 DF D6 8E E0 B7 9E 90 F2 83

      Transient Key  : 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
                       00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

      EAPOL HMAC     : FA E2 20 1F 32 93 6D AB E8 B4 68 63 0B E6 E3 C6
```

The password is `nighthawk`. Looking in the beacon frame we can see the SSID is `ATLAS_PMC`. If we go to Wireshark > Preference > Protocols > IEEE 802.11 we can add decryption keys. Add a `wpa-` type of key (note nothing following the `-`) of value `nighthawk:ATLAS_PMC`. 

When we do this we notice a PDF being downloaded. We Right Click > Copy as Hex stream and do the following:

```
galleywest:ppc/ $ vim pdf.hex
galleywest:ppc/ $ cat pdf.hex | xxd -r -p > pdf.pdf
```

Opening the PDF and scrolling to the bottom reveals our flag: `ractf{j4ck_ry4n}`