import whois

def lookup_domain(domain):
    try:
        print(f"\n🌍 WHOIS Lookup for: {domain}\n")
        info = whois.whois(domain)

        print(f"Domain Name: {info.domain_name}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Name Servers: {info.name_servers}")
        print(f"Status: {info.status}")

    except Exception as e:
        print(f"⚠️ Error fetching WHOIS data: {e}")
