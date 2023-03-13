import bitcoin
import hashlib

# Introdu adresa Bitcoin pentru care dorești să obții coordonatele ECDSA
address = "19D8wvqt8iSSXe3AmBZeLZRyEKS4EXPnZ3"

# Transformă adresa în formatul necesar pentru utilizarea în biblioteca bitcoin
address_bytes = bitcoin.base58.decode_check(address)[1:]

# Creează o cheie privată aleatorie utilizând biblioteca bitcoin
private_key = bitcoin.random_key()

# Creează o cheie publică pe baza cheii private utilizând biblioteca bitcoin
public_key = bitcoin.encode_pubkey(bitcoin.privkey_to_pubkey(private_key), "hex")

# Calculează coordonatele ECDSA x și y pe baza cheii publice utilizând biblioteca bitcoin
x, y = bitcoin.decode_pubkey(public_key)

# Afișează coordonatele ECDSA x și y
print("Coordonate ECDSA x și y:")
print(f"x: {x}")
print(f"y: {y}")
