import requests
import concurrent.futures

def find_subdomains(domain, wordlist_file="wordlist.txt"):
    try:
        with open(wordlist_file, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ Wordlist file '{wordlist_file}' not found.")
        return

    print(f"\n🔍 Searching for subdomains of: {domain}\n")

    def check_subdomain(sub):
        url = f"http://{sub}.{domain}"
        try:
            r = requests.get(url, timeout=2)
            return f"{url} ✅"
        except requests.RequestException:
            return None

    found = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(check_subdomain, subdomains)
        for result in results:
            if result:
                print(result)
                found.append(result)

    if not found:
        print("❌ No subdomains found.")
