from bitcoinlib.encoding import pubkeyhash_to_addr, addr_to_pubkeyhash
from bitcoinlib.keys import Key, HDKey
from bitcoinlib.transactions import Transaction
from bitcoinlib.wallets import Wallet

# Introdu adresa Bitcoin pentru care dorești să obții coordonatele ECDSA
address = "19D8wvqt8iSSXe3AmBZeLZRyEKS4EXPnZ3"

# Transformă adresa în formatul necesar pentru utilizarea în biblioteca bitcoinlib
address_bytes = bytes.fromhex(addr_to_pubkeyhash(address.encode('ISO-8859-1')))



# Creează o cheie privată aleatorie utilizând biblioteca bitcoinlib
key = Key(secret_exponent=bitcoinlib.random_key())

# Creează o cheie publică pe baza cheii private utilizând biblioteca bitcoinlib
public_key = key.public_hex

# Calculează coordonatele ECDSA x și y pe baza cheii publice utilizând biblioteca bitcoinlib
key_data = bytes.fromhex(public_key)
x, y = bitcoinlib.ecdsa.key_data_to_public_pair(key_data)

# Afișează coordonatele ECDSA x și y
print("Coordonate ECDSA x și y:")
print(f"x: {x}")
print(f"y: {y}")
