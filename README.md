# Cipher
This Cipher web application allows users to upload a text file from their device and encrypts the content using the Caesar Cipher.

## Usage
```bash
cd src/cipher
python3 manage.py makemigrations filemanager
python3 manage.py migrate 
python3 manage.py runserver
```
Go to: http://127.0.0.1:8000/

## Tests
In order to run the unit tests for the cipher module:
```bash
cd src/cipher/filemanager/cipher_api
python3 -m unittest discover test
```
