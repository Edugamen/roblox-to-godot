import random
import base64

def generate_uid():
    uid = random.getrandbits(64)
    uid_bytes = uid.to_bytes(8, "big")
    return base64.b32encode(uid_bytes).decode().lower().rstrip("=")