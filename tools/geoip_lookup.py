import requests

def geoip_lookup(ip):
    print(f"\n📍 GeoIP lookup for: {ip}\n")
    try:
        url = f"http://ip-api.com/json/{ip}"
        r = requests.get(url, timeout=5)
        data = r.json()

        if data["status"] == "success":
            print(f"IP: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"Latitude: {data['lat']}")
            print(f"Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Org: {data['org']}")
        else:
            print(f"❌ Error: {data.get('message', 'Unknown error')}")

    except Exception as e:
        print(f"⚠️ Error fetching GeoIP data: {e}")
