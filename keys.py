from btclib import bip32, bech32
from btclib.script import p2pkh_scriptPubKey
from btclib.tx import Tx, TxIn, TxOut
from btclib.utils import hash160

# Introdu adresa Bitcoin pentru care dorești să obții coordonatele ECDSA
address = "19D8wvqt8iSSXe3AmBZeLZRyEKS4EXPnZ3"

# Transformă adresa în formatul necesar pentru utilizarea în biblioteca btclib
hrp = "bc"
witver, witprog = bech32.decode(hrp, address)
address_bytes = bytes(bech32.convertbits(witprog, 5, 8, False))

# Creează o cheie privată aleatorie utilizând biblioteca btclib
root = bip32.HDKey.from_seed(b'')
key = root.derive("m/0")

# Creează o cheie publică pe baza cheii private utilizând biblioteca btclib
public_key = key.sec().hex()

# Calculează coordonatele ECDSA x și y pe baza cheii publice utilizând biblioteca btclib
key_data = bytes.fromhex(public_key)
x, y = key.uncompressed.sec().to_xy()

# Afișează coordonatele ECDSA x și y
print("Coordonate ECDSA x și y:")
print(f"x: {x}")
print(f"y: {y}")
