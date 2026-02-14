import requests

BASE_URL = "https://api.worldbank.org/v2"

INDICATORS = [
    "NY.GDP.MKTP.CD",   # GDP
    "SP.POP.TOTL",      # Population
    "FP.CPI.TOTL.ZG",   # Inflation
    "SL.UEM.TOTL.ZS"    # Unemployment
]


def fetch_paginated_data(url):
    all_records = []
    page = 1

    while True:
        paginated_url = f"{url}&page={page}"
        response = requests.get(paginated_url)
        response.raise_for_status()

        data = response.json()

        if len(data) < 2:
            break

        metadata = data[0]
        records = data[1]

        all_records.extend(records)

        if page >= metadata["pages"]:
            break

        page += 1

    return all_records


def fetch_indicator(indicator_code):
    print(f"Fetching {indicator_code}...")

    url = (
        f"{BASE_URL}/country/all/indicator/"
        f"{indicator_code}?format=json&per_page=20000"
    )

    records = fetch_paginated_data(url)

    print(f"  Retrieved {len(records)} records.")
    return records


def fetch_world_bank_data():
    print("Fetching World Bank data...")

    all_records = []

    for indicator in INDICATORS:
        records = fetch_indicator(indicator)
        all_records.extend(records)

    print(f"\nTotal records fetched: {len(all_records)}")
    return all_records


def fetch_country_metadata():
    print("Loading country metadata...")

    url = f"{BASE_URL}/country?format=json&per_page=400"
    countries = fetch_paginated_data(url)

    # DEBUG — inspect AFE
    for country in countries:
        if country["id"] == "AFE":
            print("AFE metadata:")
            print(country)

    real_country_iso3 = {
        country["id"]
        for country in countries
        if country["region"]["value"] != "Aggregates"
    }

    print(f"Loaded {len(real_country_iso3)} real countries.")
    return real_country_iso3
