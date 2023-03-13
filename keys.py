import bitcoin
import ecdsa

# definim adresa Bitcoin
addr = '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa'

# convertim adresa in format binar
addr_bin = bitcoin.b58check_to_bin(addr)

# generam cheia publica si punctul de pe curba SECP256k1
vk = ecdsa.VerifyingKey.from_string(addr_bin[1:], curve=ecdsa.SECP256k1)
x, y = vk.pubkey.point.x(), vk.pubkey.point.y()

# afisam coordonatele in format zecimal
print(f'Coordonatele pentru adresa {addr} sunt:')
print(f'x = {x}')
print(f'y = {y}')
