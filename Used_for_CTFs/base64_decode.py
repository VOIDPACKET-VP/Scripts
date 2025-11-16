import base64
import zlib
from itsdangerous import base64_decode

def decode_flask_session(session_cookie):
    try:
        # Split the cookie: data.timestamp.signature
        data = session_cookie.split('.')[0]
        
        # Add padding for base64
        data += '=' * (-len(data) % 4)
        
        # Decode base64
        decoded = base64.b64decode(data)
        
        # Try to decompress (Flask sessions are often compressed)
        try:
            decompressed = zlib.decompress(decoded)
            return decompressed.decode('utf-8')
        except:
            return decoded.decode('utf-8')
            
    except Exception as e:
        return f"Error: {e}"

# Your session cookie
session_cookie = ""

decoded = decode_flask_session(session_cookie)
print("Decoded session:", decoded)