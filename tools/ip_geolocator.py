import requests

def geolocate_ip(ip):
    print(f"\n🗺 Geolocation for IP: {ip}\n")
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
            print(f"❌ Error: {data['message']}")

    except Exception as e:
        print(f"⚠️ Error fetching geolocation: {e}")
