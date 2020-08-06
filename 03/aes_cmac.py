from Cryptodome.Hash import CMAC
from Cryptodome.Cipher import AES
import binascii


def get_challenge():
    secret = binascii.a2b_hex('00112233445566778899aabbccddeeff')
    cobj = CMAC.new(secret, ciphermod=AES)
    msg = binascii.a2b_hex('2c26c50065650077') + binascii.a2b_hex(str('%08x' % 133653632)) + binascii.a2b_hex(
        str('%08x' % 0))
    cobj.update(msg)
    btr = cobj.digest()
    print(btr.__len__())
    ch = ''
    for x in range(0, 16):
        ch += ('%02X' % btr[16 - x - 1])
    print(ch)
    challenge = cobj.hexdigest()
    print(challenge)

    index = 0
    length = len(challenge)
    al = []
    for i in range(index, length, 2):
        b = challenge[length - 2 - i:length - i]
        al.append(b)

    print("".join(al))


def crc16(x, invert):
    a = 0xFFFF
    b = 0xA001
    for byte in x:
        a ^= byte
        for i in range(8):
            last = a % 2
            a >>= 1
            if last == 1:
                a ^= b
    s = hex(a).upper()

    return s[4:6] + s[2:4] if invert == True else s[2:4] + s[4:6]

print(crc16("012345678", True))
print(crc16("012345678", False))
print(crc16("010600010017", True))