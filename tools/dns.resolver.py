import dns.resolver

def resolve_dns(domain):
    print(f"\n📡 DNS Records for: {domain}\n")
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"{record} Records:")
            for rdata in answers:
                print(f"  - {rdata}")
        except dns.resolver.NoAnswer:
            print(f"{record} Records: ❌ No answer")
        except dns.resolver.NXDOMAIN:
            print(f"{record} Records: ❌ Domain does not exist")
        except Exception as e:
            print(f"{record} Records: ⚠️ Error - {e}")
