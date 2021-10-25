from hashlib import sha256

hash_value = input("Enter the hash value(SHA2546): ")
wordlist = ['sathvik','sai','techtuber','twitter','nullshock','jon']

flag=False
val=""
for word in wordlist:
    value = sha256(word.encode())
    if hash_value == value.hexdigest():
        flag=True
        val=word
        break

if flag:
    print(val)
else:
    print("Not possible")
