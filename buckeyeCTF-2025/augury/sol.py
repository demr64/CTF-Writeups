from pathlib import Path

x = 3404970675
b = 3553295105
mod = 2**32

PNG_SIG = bytes([0x89, 0x50, 0x4E, 0x47])

def generate_keystream(i):
    return (i * x + b) % mod

def decrypt_from_hex(hexdata: str, out_path: str = "recovered.png"):
    data = bytearray(bytes.fromhex(hexdata.strip()))
    p0 = PNG_SIG[0:4]
    c0 = bytes(data[0:4])
    k0 = int.from_bytes(bytes(x ^ y for x, y in zip(c0, p0)), byteorder="big")
    ks = k0

    for i in range(0, len(data), 4):
        key_bytes = ks.to_bytes(4, byteorder="big")
        for j in range(4):
            if i + j >= len(data):
                break
            data[i + j] ^= key_bytes[j]
        ks = generate_keystream(ks)

    Path(out_path).write_bytes(data)

if __name__ == "__main__":
    with open("secret_pic.txt", "r") as f:
        h = f.readline()
    decrypt_from_hex(h)

