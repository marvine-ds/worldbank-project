def clean_data(records, real_country_codes):
    cleaned = []

    for record in records:

        # Skip records with no value
        if record["value"] is None:
            continue

        country_code = record["countryiso3code"]
        country_name = record["country"]["value"]
        indicator_code = record["indicator"]["id"]
        indicator_name = record["indicator"]["value"]
        year = int(record["date"])
        value = float(record["value"])

        # Determine if aggregate using ISO3 whitelist
        is_aggregate = country_code not in real_country_codes

        cleaned.append((
            country_code,
            country_name,
            year,
            indicator_code,
            indicator_name,
            value,
            is_aggregate
        ))

    print(f"Cleaned records: {len(cleaned)}")
    return cleaned
