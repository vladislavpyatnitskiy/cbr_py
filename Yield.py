import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def cbr_yields(s, e):
  
    # Construct the URL
    url = (f"https://www.cbr.ru/eng/hd_base/zcyc_params/?UniDbQuery.Posted="
           f"True&UniDbQuery.From={s}&UniDbQuery.To={e}")
    
    # Fetch and parse the HTML
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all td elements
    td_elements = soup.find_all('td')
    B = [td.get_text(strip=True) for td in td_elements]
    
    # Create DataFrame by grouping elements in chunks of 13
    data = []
    for i in range(0, len(B), 13):
        if i + 13 <= len(B):
            data.append(B[i:i+13])
    
    # Create DataFrame with proper column names
    columns = [
      "Date", "3M", "6M", "9M", "1Y", "2Y", "3Y", 
      "5Y","7Y", "10Y", "15Y", "20Y", "30Y"
    ]
      
    v = pd.DataFrame(data, columns=columns)
    
    # Convert Date column to datetime
    v['Date'] = pd.to_datetime(v['Date'], format='%d.%m.%Y')
    
    # Sort by date in ascending order
    v = v.sort_values('Date', ascending=True)
    
    # Set Date as index and remove the column
    v = v.set_index('Date')
    
    return v

cbr_yields("10.09.2025", "25.09.2025") # Example usage
