import requests
import bitcoinlib.keys as keys
from bitcoinlib.encoding import to_bytes, to_hex

# Introduceți adresa Bitcoin pentru care doriți să recuperați semnătura ECDSA R, S, Z
address = "113324vM6NBar2q72w6iDCdQvPnPQw8Tvw"

# Descărcați tranzacțiile asociate cu adresa utilizând API-ul blockchain.info
txs = requests.get(f"https://blockchain.info/address/{address}?format=json").json()["txs"]

# Recuperați semnăturile pentru fiecare tranzacție
for tx in txs:
    raw_tx = requests.get(f"https://blockchain.info/rawtx/{tx['hash']}").json()
    for input in raw_tx["inputs"]:
        if input["prev_out"]["addr"] == address:
            # Recuperați semnătura R, S, Z din scriptSig
            scriptSig = input["script"]
            sig = keys.parse_scriptSig(scriptSig)
            sig_der = sig[0]
            sig_hash_type = sig[1]
            r = to_hex(to_bytes(sig_der[0], 32))
            s = to_hex(to_bytes(sig_der[1], 32))
            z = to_hex(to_bytes(sig_hash_type, 1))
            print(f"Tranzacția: {tx['hash']}")
            print(f"Semnătură R: {r}")
            print(f"Semnătură S: {s}")
            print(f"Semnătură Z: {z}")
