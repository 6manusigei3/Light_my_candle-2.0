import shodan

def shodan_lookup(api_key, query):
    print(f"\n🕵️ Shodan search for: {query}\n")
    try:
        api = shodan.Shodan(api_key)
        results = api.search(query)

        print(f"Total results: {results['total']}\n")

        for match in results['matches'][:10]:  # Limit to first 10 results
            ip_str = match.get('ip_str', 'N/A')
            port = match.get('port', 'N/A')
            org = match.get('org', 'N/A')
            data = match.get('data', '').strip()
            print(f"IP: {ip_str}")
            print(f"Port: {port}")
            print(f"Org: {org}")
            print(f"Banner:\n{data}")
            print("-" * 40)

    except shodan.APIError as e:
        print(f"❌ Shodan API Error: {e}")
