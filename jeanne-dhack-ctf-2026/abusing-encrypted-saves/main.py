import base64
secure_save = "744PA3kQNaGuCBM9ymiDnPWhIZKGNQkXrEgAPKVzBxRC+X8o7MMG4Kj4s4nBoUx1Zk/S83bbfU8UDG8E1toJolfFOkhaofj1xEO+mGrlVavmGtIkdEgOWA=="
ct = base64.b64decode(secure_save)
ct = bytearray(ct)
print(ct)
pt = b'{"wins": "000", "losses": "000", "draws": "000", "total_games": "000", "winrate": "0.0"}'

offset = pt.index(b'"total_games": "000"') + len('"total_games": "')
ct[offset] ^=  ord('0') ^ord('1') 


offset = pt.index(b'"winrate": "0.0"') + len('"winrate": "')

ct[offset] ^= ord('0') ^ord('1') 
ct[offset+1] ^= ord('.') ^ord('0') 


print(base64.b64encode(ct))
