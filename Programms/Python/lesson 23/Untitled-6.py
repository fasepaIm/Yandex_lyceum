def encrypt_caesar(msg, shift):
    msgg = []
    for i in msg:
        if 1040 <= ord(i) <= 1103:
            if 1040 <= ord(i) <= 1071:
                if ord(i) + shift <= 1071:
                    msgg.append(chr(ord(i) + shift))
                else:
                    msgg.append(chr(1039 + ((ord(i) + shift) - 1071)))
            elif 1072 <= ord(i) <= 1103:
                if ord(i) + shift <= 1103:
                    msgg.append(chr(ord(i) + shift))
                else:
                    msgg.append(chr(1071 + ((ord(i) + shift) - 1103)))
        else:
            msgg.append(i)
    return ''.join(msgg)


def decrypt_caesar(msg, shift):
    msgg = []
    for i in msg:
        if 1040 <= ord(i) <= 1103:
            if 1040 <= ord(i) <= 1071:
                if ord(i) - shift >= 1040:
                    msgg.append(chr(ord(i) - shift))
                else:
                    msgg.append(chr(1072 - (1040 - (ord(i) - shift))))
            elif 1072 <= ord(i) <= 1103:
                if ord(i) - shift >= 1072:
                    msgg.append(chr(ord(i) - shift))
                else:
                    msgg.append(chr(1104 - (1072 - (ord(i) - shift))))
        else:
            msgg.append(i)
    return ''.join(msgg)