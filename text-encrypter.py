#!/usr/bin/env python3

import argparse
import hashlib
import base64
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# ---------------- AES ---------------- #

def aes_encrypt(text, key):
    key = key.encode().ljust(16)[:16]
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct).decode()

def aes_decrypt(ciphertext, key):
    key = key.encode().ljust(16)[:16]
    raw = base64.b64decode(ciphertext)
    iv = raw[:16]
    ct = raw[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode()

# ---------------- DES ---------------- #

def des_encrypt(text, key):
    key = key.encode().ljust(8)[:8]
    cipher = DES.new(key, DES.MODE_CBC)
    ct = cipher.encrypt(pad(text.encode(), DES.block_size))
    return base64.b64encode(cipher.iv + ct).decode()

def des_decrypt(ciphertext, key):
    key = key.encode().ljust(8)[:8]
    raw = base64.b64decode(ciphertext)
    iv = raw[:8]
    ct = raw[8:]
    cipher = DES.new(key, DES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), DES.block_size)
    return pt.decode()

# ---------------- HASHES ---------------- #

def hash_text(text, algo):

    if algo == "md5":
        return hashlib.md5(text.encode()).hexdigest()

    if algo == "sha256":
        return hashlib.sha256(text.encode()).hexdigest()

    if algo == "sha512":
        return hashlib.sha512(text.encode()).hexdigest()

# ---------------- RSA ---------------- #

def generate_rsa():
    key = RSA.generate(2048)

    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)

    with open("public.pem", "wb") as f:
        f.write(public_key)

    print("Keys generated: private.pem / public.pem")

def rsa_encrypt(text, pubfile):

    pubkey = RSA.import_key(open(pubfile).read())
    cipher = PKCS1_OAEP.new(pubkey)

    ct = cipher.encrypt(text.encode())

    return base64.b64encode(ct).decode()

def rsa_decrypt(ciphertext, privfile):

    privkey = RSA.import_key(open(privfile).read())
    cipher = PKCS1_OAEP.new(privkey)

    ct = base64.b64decode(ciphertext)

    pt = cipher.decrypt(ct)

    return pt.decode()

# ---------------- CLI ---------------- #

def main():

    parser = argparse.ArgumentParser(
        description="Simple encryption Tool"
    )

    parser.add_argument("-a", "--algo",
                        help="Algorithm: aes, des, rsa, md5, sha256, sha512")

    parser.add_argument("-e", "--encrypt",
                        help="Encrypt text")

    parser.add_argument("-d", "--decrypt",
                        help="Decrypt text")

    parser.add_argument("-k", "--key",
                        help="Secret key")

    parser.add_argument("-p", "--pub",
                        help="Public key file")

    parser.add_argument("-r", "--priv",
                        help="Private key file")

    parser.add_argument("--genrsa",
                        action="store_true",
                        help="Generate RSA keypair")

    args = parser.parse_args()

    if args.genrsa:
        generate_rsa()
        return

    if args.encrypt:

        if args.algo == "aes":
            print(aes_encrypt(args.encrypt, args.key))

        elif args.algo == "des":
            print(des_encrypt(args.encrypt, args.key))

        elif args.algo == "rsa":
            print(rsa_encrypt(args.encrypt, args.pub))

    elif args.decrypt:

        if args.algo == "aes":
            print(aes_decrypt(args.decrypt, args.key))

        elif args.algo == "des":
            print(des_decrypt(args.decrypt, args.key))

        elif args.algo == "rsa":
            print(rsa_decrypt(args.decrypt, args.priv))

    elif args.algo in ["md5","sha256","sha512"]:
        print(hash_text(args.encrypt, args.algo))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()