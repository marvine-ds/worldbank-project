from fetch import fetch_world_bank_data, fetch_country_metadata
from cleandata import clean_data
from load_to_mysql import insert_data


if __name__ == "__main__":
    print("Main file is running...")

    real_country_codes = fetch_country_metadata()
    raw_records = fetch_world_bank_data()
    cleaned_records = clean_data(raw_records, real_country_codes)

    insert_data(cleaned_records)





