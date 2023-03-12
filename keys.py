from bitcoinlib.encoding import pubkeyhash_to_addr, addr_to_pubkeyhash
from bitcoinlib.keys import Key, HDKey
from bitcoinlib.transactions import Transaction, Input, Output

# Introdu adresa Bitcoin pentru care dorești să obții coordonatele ECDSA
address = "19D8wvqt8iSSXe3AmBZeLZRyEKS4EXPnZ3"

# Transformă adresa în formatul necesar pentru utilizarea în biblioteca bitcoinlib
address_bytes = bytes.fromhex(addr_to_pubkeyhash(address))

# Creează o cheie privată aleatorie utilizând biblioteca bitcoinlib
key = Key(secret_exponent=HDKey.create_master(b'').generate_key().secret_exponent)

# Creează o cheie publică pe baza cheii private utilizând biblioteca bitcoinlib
public_key = key.public_key.hex()

# Calculează coordonatele ECDSA x și y pe baza cheii publice utilizând biblioteca bitcoinlib
key_data = bytes.fromhex(public_key)
x, y = key.pubkey.to_xy()

# Afișează coordonatele ECDSA x și y
print("Coordonate ECDSA x și y:")
print(f"x: {x}")
print(f"y: {y}")
