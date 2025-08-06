import hashlib

def hash_string(algorithm, input_str):
    try:
        hash_func = getattr(hashlib, algorithm)
        hash_value = hash_func(input_str.encode()).hexdigest()
        print(f"{algorithm.upper()} hash: {hash_value}")
    except AttributeError:
        print(f"❌ Unsupported algorithm: {algorithm}")
    except Exception as e:
        print(f"⚠️ Error hashing string: {e}")
