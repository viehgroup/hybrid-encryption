VIEH HYBRID ENCRYPTION PROJECT

The main aim of this project is to make files more secure by using hybrid encryption, and to
provide integrity of data.

Hybrid Encryption Include:-
∙ AES
Encryption Algorithm
∙ RSA Encryption Algorithm

Background working of tool
1. Creates directories and files for generated RSA and AES keys and store it.
2. For encryption takes the AES key file reads it and decrypt it using RSA private key and then
encrypt the selected file using AES key and store at local system.
3. For decryption takes the AES key file reads it and decrypt it using RSA private key and then
decrypts the selected file using AES key and store at local system.

Requirements:-
Step 1:- Download the tool from given Link.
Step 2:-Download pip packageStep 3:- Frist install the Prerequisites Crypto Packages for Linux/Windows by using Terminal
/Command Prompt.

For Linux:
∙ pip install pycryptodome
∙ pip install Crypto
∙ pip install ttkthemes

For Windows:
∙ pip install pycryptodome
∙ pip install cryptography
∙ pip install paramiko
∙ pip install pycryptodomex
∙ pip install ttkthemes

Once Completed this steps, You have successfully installed the program and now can run it
Run python setup.py in cmd/terminal

Use of Tool:-
For Encryption:
Step 1:- Select the file first.
Step 2:- Choose the option Encryption.
Step 3:- The file has been encrypted in a folder in the user of C drive with extension(.enc)
and you get the message accordingly.

For Decryption:
Step 1:- Select the file from the folder in user of C drive with
extension(.enc) Step 2:- Choose the option Decryption.
Step 3:- The file has decrypted in folder in user of C drive and you got the message
accordingly.
