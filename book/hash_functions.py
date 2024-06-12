
import hashlib

def sha256_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
