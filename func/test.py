from genqrcode import generate_qr_code
from aes import encrypt,decrypt
import base64

import secrets

def generate_256bit_bytes():
    # Tạo 32 byte ngẫu nhiên (256 bit)
    random_bytes = secrets.token_bytes(32)
    
    return random_bytes

# Sử dụng hàm để tạo chuỗi byte
x = generate_256bit_bytes()

# In chuỗi byte
print(x)