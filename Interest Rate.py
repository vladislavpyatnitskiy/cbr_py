import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def cbr_interest_rate(start_date, end_date):
    """
    Fetch CBR key interest rate data.

    Parameters:
        start_date (str): format 'dd.mm.yyyy'
        end_date (str): format 'dd.mm.yyyy'

    Returns:
        pd.DataFrame
    """

    # Minimum allowed date
    min_date = datetime.strptime("17.09.2013", "%d.%m.%Y")
    start_dt = datetime.strptime(start_date, "%d.%m.%Y")

    if start_dt < min_date:
        start_date = "17.09.2013"

    url = (
        f"https://www.cbr.ru/eng/hd_base/KeyRate/"
        f"?UniDbQuery.Posted=True&UniDbQuery."
        f"From={start_date}&UniDbQuery.To={end_date}"
    )

    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Find the main table
    table = soup.find("table")
    if table is None:
        raise ValueError("No table found on the page")

    rows = []

    for tr in table.find_all("tr")[1:]:  # skip header
        cols = [td.get_text(strip=True) for td in tr.find_all("td")]
        if len(cols) == 2:
            rows.append(cols)

    df = pd.DataFrame(rows, columns=["Date", "Interest Rate"])

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"], format="%d.%m.%Y")

    # Convert interest rate to numeric
    df["Interest Rate"] = (
        df["Interest Rate"]
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    # Sort ascending
    df = df.sort_values("Date")

    # Set date as index
    df.set_index("Date", inplace=True)

    return df

cbr_interest_rate("18.11.2024", "28.10.2025") # Example usage
