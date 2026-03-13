# Text Encrypter 🔐

Text Encrypter is a simple **Python command-line cryptography tool** that allows users to encrypt and decrypt text using different encryption algorithms.
This project was created as a **cybersecurity learning project** to understand how encryption and hashing work in practice.

The tool supports both **symmetric encryption** and **asymmetric encryption**, as well as some hashing algorithms.

Supported algorithms:

* **Advanced Encryption Standard (AES)** – symmetric encryption
* **Data Encryption Standard (DES)** – symmetric encryption
* **RSA Cryptosystem (RSA)** – asymmetric encryption
* **MD5** – hashing algorithm
* **SHA-256** – hashing algorithm
* **SHA-512** – hashing algorithm

This tool is intended for **learning cryptography concepts and experimenting with encryption techniques**.

---

<img width="1240" height="395" alt="image" src="https://github.com/user-attachments/assets/7537aa5e-b1a6-48ca-940b-b786a9de6a1d" />


# Requirements

Python 3 is required.

Install the required library:

```bash
pip install pycryptodome
```

Built-in Python modules used:

* argparse
* hashlib
* base64

---

# Usage

Run the script from the terminal:

```bash
python text-encrypter.py [options]
```

Show help menu:

```bash
python text-encrypter.py -h
```

---

# Command Options

| Option     | Description                                           |
| ---------- | ----------------------------------------------------- |
| `-a`       | Select algorithm (aes, des, rsa, md5, sha256, sha512) |
| `-e`       | Encrypt text                                          |
| `-d`       | Decrypt text                                          |
| `-k`       | Secret key (for AES / DES)                            |
| `-p`       | Public key file (for RSA encryption)                  |
| `-r`       | Private key file (for RSA decryption)                 |
| `--genrsa` | Generate RSA public and private key pair              |

---

# Examples

### AES Encryption

```bash
python text-encrypter.py -a aes -e "hello world" -k mysecretkey
```

### AES Decryption

```bash
python text-encrypter.py -a aes -d "<ciphertext>" -k mysecretkey
```

---

### DES Encryption

```bash
python text-encrypter.py -a des -e "hello" -k mykey
```

---

### Generate RSA Keys

```bash
python text-encrypter.py --genrsa
```

This generates:

```
public.pem
private.pem
```

---

### RSA Encryption

```bash
python text-encrypter.py -a rsa -e "secret message" -p public.pem
```

---

### RSA Decryption

```bash
python text-encrypter.py -a rsa -d "<ciphertext>" -r private.pem
```

---


