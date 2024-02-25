# Encrypter
A Python program for encrypting files by changing every byte to a different one according to a table. The table is generated randomly using a PRNG with a seed that can be specified by the user and works as a key to generate an inverse table that can be used to decrypt the file.

## Download
```bash
git clone https://github.com/Stachu1/Encrypter.git
```

## Usage
**Encrypting**
```bash
python Encrypter.py <file> enc <key>
```
This will create a copy of the file with a .encrypted extension

**Decrypting**
```bash
python Encrypter.py <file.encrypted> dec <key>
```
This will create a decrypted copy of the file

<img width="600" alt="image" src="https://github.com/Stachu1/Encrypter/assets/77758413/d62d4a33-5697-4172-8187-3551e69436d6">

**I DO NOT RECOMMEND USING IT FOR STUFF THAT ACCTUALLY NEEDS TO BE ENCRYPTED, AS IT IS PROBABLY NOT SECURE**
Still it was a fun project ;)
