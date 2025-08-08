import requests

def subdomain_enum(domain, wordlist_path):
    print(f"\n🌐 Enumerating subdomains for: {domain}\n")
    try:
        with open(wordlist_path, "r") as f:
            words = f.read().splitlines()

        for word in words:
            subdomain = f"{word}.{domain}"
            try:
                url = f"http://{subdomain}"
                r = requests.get(url, timeout=2)
                if r.status_code < 400:
                    print(f"✅ Found: {subdomain}")
            except requests.ConnectionError:
                pass  # Ignore if not reachable
            except Exception as e:
                print(f"⚠️ Error: {e}")

    except FileNotFoundError:
        print(f"❌ Wordlist file not found: {wordlist_path}")
