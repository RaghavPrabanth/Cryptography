#Encryption

l1=['0B85','0B86','0B87','0B88','0B89','0B8A','0B8E','0B8F','0B90','0B92','0B93','0B94',
    '0B95','0B99','0B9A','0B9E','0B9F','0BA3','0BA4','0BA8','0BAA','0BAE','0BAF','0BB0',
    '0BB2','0BB5','0BB3','0B84','0BB1','0BA9']
print(l1)

plaintext=input("enter the value of 8 bit pixels:")
print(plaintext)

byte1=int(plaintext[0:4],2)
byte2=int(plaintext[4:8],2)
print(byte1,byte2)


key=input("enter 32 bit key:")
print(key)

key1=key[0:2]
key2=key[2:4]
key3=key[4:6]
key4=key[6:8]
key5=key[8:10]
key6=key[10:12]
key7=key[12:14]
key8=key[14:16]
key9=key[16:18]
key10=key[18:20]
key11=key[20:22]
key12=key[22:24]
key13=key[24:26]
key14=key[26:28]
key15=key[28:30]
key16=key[30:32]


x=[key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15,key16]

y=int(x[byte1])
z=int(x[byte2])
print("Cipher text:",l1[y],l1[z])


#Decryption

l1=['0B85','0B86','0B87','0B88','0B89','0B8A','0B8E','0B8F','0B90','0B92','0B93','0B94',
    '0B95','0B99','0B9A','0B9E','0B9F','0BA3','0BA4','0BA8','0BAA','0BAE','0BAF','0BB0',
    '0BB2','0BB5','0BB3','0B84','0BB1','0BA9']
print(l1)

ciphertext=input("enter the value of 8 bit Ciphertext:")
print(ciphertext)

cbyte1=ciphertext[0:4]
cbyte2=ciphertext[4:8]
print(cbyte1,cbyte2)

key=input("enter 32 bit key:")
print(key)

key1=key[0:2]
key2=key[2:4]
key3=key[4:6]
key4=key[6:8]
key5=key[8:10]
key6=key[10:12]
key7=key[12:14]
key8=key[14:16]
key9=key[16:18]
key10=key[18:20]
key11=key[20:22]
key12=key[22:24]
key13=key[24:26]
key14=key[26:28]
key15=key[28:30]
key16=key[30:32]


x=[key1,key2,key3,key4,key5,key6,key7,key8,key9,key10,key11,key12,key13,key14,key15,key16]




for i in range(0,30):
    if cbyte1 == l1[i]:
        cval1 = i
    if cbyte2 == l1[i]:
        cval2 = i

for j in range(0,16):
    if cval1 == int(x[j]):
        ist1 = j
    if cval2 == int(x[j]):
        ist2 = j

print(ist1,ist2)


byte1 =bin(ist1)[2:].zfill(4)
byte2 =bin(ist2)[2:].zfill(4)
print("Plaintext :", byte1, byte2)
