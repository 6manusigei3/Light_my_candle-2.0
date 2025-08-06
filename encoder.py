import base64
import urllib.parse

def process_encoding(encoding_type, string, decode=False):
    try:
        if encoding_type == 'base64':
            if decode:
                decoded = base64.b64decode(string).decode()
                print(f"Base64 Decoded: {decoded}")
            else:
                encoded = base64.b64encode(string.encode()).decode()
                print(f"Base64 Encoded: {encoded}")

        elif encoding_type == 'url':
            if decode:
                decoded = urllib.parse.unquote(string)
                print(f"URL Decoded: {decoded}")
            else:
                encoded = urllib.parse.quote(string)
                print(f"URL Encoded: {encoded}")

        else:
            print("❌ Unsupported encoding type.")

    except Exception as e:
        print(f"⚠️ Error in encoding/decoding: {e}")
