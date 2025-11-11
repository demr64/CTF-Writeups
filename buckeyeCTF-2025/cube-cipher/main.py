from pwn import *

HOST = "cube-cipher.challs.pwnoh.io"
PORT = 1337 
def attempt(payload):
    p = remote(HOST, PORT, timeout=3, ssl=True)
    for i in range(0, 100):
        p.recvuntil(b'Option: ')
        p.sendline(b'4')
        p.recvuntil(b'Option: ')

        p.sendline(payload)
        
        data = b""
        while True:
            chunk = p.recv(128)  
            data += chunk
            if b'Option: ' in chunk:
                break
        
        print(bytes.fromhex(data[:54].decode()))

if __name__ == '__main__':
    payload = b'3'
    resp = attempt(payload)
