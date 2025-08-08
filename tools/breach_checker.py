import requests

def check_breaches(email):
    print(f"\n🔍 Checking breaches for: {email}\n")
    try:
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        headers = {
            "hibp-api-key": "YOUR_API_KEY",  # Replace or load from env
            "User-Agent": "CyberToolbox"
        }
        r = requests.get(url, headers=headers, timeout=5)

        if r.status_code == 404:
            print("✅ No breaches found!")
        elif r.status_code == 200:
            breaches = r.json()
            print(f"⚠️ Found {len(breaches)} breaches:")
            for breach in breaches:
                print(f"- {breach['Name']} ({breach['BreachDate']})")
                print(f"  Description: {breach['Description']}\n")
        else:
            print(f"❌ Error: {r.status_code} - {r.text}")

    except Exception as e:
        print(f"⚠️ Error checking breaches: {e}")
