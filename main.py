import argparse
from tools import hasher, encoder, portscanner, whois_lookup, dns_resolver, password_checker

def main():
    parser = argparse.ArgumentParser(
        description='🛡️ Cybersecurity Toolbox CLI - Modular Security Tools in One Place'
    )
    subparsers = parser.add_subparsers(dest='command', help='Available tools')

    # Hasher
    hash_parser = subparsers.add_parser('hash', help='Generate hash from string')
    hash_parser.add_argument('-a', '--algorithm', choices=['md5', 'sha1', 'sha256'], required=True, help='Hash algorithm')
    hash_parser.add_argument('-s', '--string', required=True, help='Input string to hash')

    # Encoder
    encode_parser = subparsers.add_parser('encode', help='Base64 or URL encode/decode a string')
    encode_parser.add_argument('-t', '--type', choices=['base64', 'url'], required=True, help='Encoding type')
    encode_parser.add_argument('-s', '--string', required=True, help='Input string')
    encode_parser.add_argument('--decode', action='store_true', help='Decode instead of encode')

    # Port Scanner
    port_parser = subparsers.add_parser('scan', help='Scan common ports on a host')
    port_parser.add_argument('--host', required=True, help='Target host (IP or domain)')
    port_parser.add_argument('--ports', default='22,80,443', help='Comma-separated list of ports')

    # WHOIS
    whois_parser = subparsers.add_parser('whois', help='WHOIS lookup for a domain')
    whois_parser.add_argument('--domain', required=True, help='Target domain')

    # DNS Resolver
    dns_parser = subparsers.add_parser('dns', help='Resolve DNS records for a domain')
    dns_parser.add_argument('--domain', required=True, help='Target domain')

    # Password Checker
    pw_parser = subparsers.add_parser('password', help='Check password strength')
    pw_parser.add_argument('--password', required=True, help='Password to evaluate')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == 'hash':
            hasher.hash_string(args.algorithm, args.string)
        elif args.command == 'encode':
            encoder.process_encoding(args.type, args.string, args.decode)
        elif args.command == 'scan':
            portscanner.scan_ports(args.host, args.ports)
        elif args.command == 'whois':
            whois_lookup.lookup_domain(args.domain)
        elif args.command == 'dns':
            dns_resolver.resolve_domain(args.domain)
        elif args.command == 'password':
            password_checker.check_strength(args.password)
        else:
            print("❌ Unknown command.")
            parser.print_help()
    except Exception as e:
        print(f"⚠️ Error: {e}")

if _name_ == '_main_':
    main()
