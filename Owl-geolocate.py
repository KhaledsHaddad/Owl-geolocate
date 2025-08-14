#!/usr/bin/env python3
import requests
import sys
import json

def banner():
    print("""
    ╔══════════════════════════════════════════════╗
    ║              OWL-GEOLOCATE v1.0              ║
    ║      by khaled.s.haddad | khaledhaddad.tech  ║
    ╚══════════════════════════════════════════════╝
    """)

def get_geo(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()
        if data['status'] == 'fail':
            return None
        return {
            "IP": ip,
            "Country": data.get("country", "N/A"),
            "City": data.get("city", "N/A"),
            "Region": data.get("regionName", "N/A"),
            "Latitude": data.get("lat", "N/A"),
            "Longitude": data.get("lon", "N/A"),
            "ISP": data.get("isp", "N/A"),
            "Org": data.get("org", "N/A"),
        }
    except Exception as e:
        return None

def print_result(info):
    print(f"\n[+] IP Address: {info['IP']}")
    print(f"    ├ Country  : {info['Country']}")
    print(f"    ├ Region   : {info['Region']}")
    print(f"    ├ City     : {info['City']}")
    print(f"    ├ Latitude : {info['Latitude']}")
    print(f"    ├ Longitude: {info['Longitude']}")
    print(f"    ├ ISP      : {info['ISP']}")
    print(f"    └ Org      : {info['Org']}")

def save_result(info, file_name):
    with open(file_name, 'a') as f:
        json.dump(info, f)
        f.write('\n')

def main():
    banner()
    if len(sys.argv) != 2:
        print("Usage: python3 owl-geolocate.py <ip-or-ip-list.txt>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        with open(target, 'r') as file:
            ips = [line.strip() for line in file if line.strip()]
    except:
        ips = [target]

    for ip in ips:
        info = get_geo(ip)
        if info:
            print_result(info)
            save_result(info, "geolocation_results.json")
        else:
            print(f"[!] Failed to retrieve data for {ip}")

if __name__ == "__main__":
    main()

