import pwn

#pwn.context.log_level = 'debug'


for i in range(0,101):
    r = pwn.remote("insanity1.chujowyc.tf", 4004)

    # Get starter question
    r.recvuntil("2: ")
    # Answer starter question
    r.send("4\n")

    # Start guessing the number
    r.recvuntil("?\n")
    r.send(f"{i}\n")
    response = r.recv()
    
    print(f"Tried {i}, got {response}")

#Tried 81, got b'xD xD The answer to the next one is in front of your eyes xD xD\nThe answer is 42123 ;)\r                         \rWhat is 2+2: '
# > 42123
# Congratulations the flag is: chCTF{Ez3_cha113ng3}
