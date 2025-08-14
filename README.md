# 🦉 OWL-GEOLOCATE v1.0

**Author:** khaled.s.haddad  
**Website:** [khaledhaddad.tech](https://khaledhaddad.tech)  
**Category:** Geolocation / Reconnaissance  
**Style:** Terminal Tool – Fast & Simple

---

## 📌 Overview

**OWL-GEOLOCATE** is a fast and lightweight IP geolocation tool built in Python.  
It uses `ip-api.com` to fetch detailed location and network information for a single IP address or a list of IPs.  

It's ideal for use in reconnaissance or for network analysts during OSINT or red team operations.

---

## 🧪 Features

- 🔍 Fetch:
  - Country, Region, City
  - Latitude & Longitude
  - ISP & Organization info
- 🧾 Save results to `geolocation_results.json`
- 📁 Support single IP or `.txt` list of IPs
- ⚡ Fast & minimal terminal output
- ❌ Gracefully handles failures and unreachable IPs

---

## 📦 Requirements

- Python 3.x  
- `requests` library

Install dependencies:

```bash
pip install requests

