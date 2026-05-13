# Data Retrieval for Central Bank of Russia's Data

Welcome to the repository! Here you find a collection of scripts that enable to retrieve data from Central Bank of Russia's Website.

## Bond Zero Coupon Yield Curve Data

```
cbr_yields("10.09.2025", "25.09.2025").head(5)
```
```
               3M     6M     9M     1Y  ...    10Y    15Y    20Y    30Y
Date                                    ...                            
2025-09-10  14.70  14.07  13.71  13.52  ...  13.74  13.70  13.68  13.70
2025-09-11  15.10  14.39  13.97  13.74  ...  13.81  13.76  13.72  13.71
2025-09-12  15.50  14.75  14.31  14.06  ...  13.97  13.92  13.89  13.91
2025-09-15  14.91  14.29  13.96  13.79  ...  14.09  14.06  14.05  14.08
2025-09-16  15.20  14.60  14.26  14.07  ...  14.14  14.10  14.07  14.07

[5 rows x 12 columns]
```
