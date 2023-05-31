# cli installation:
# pip install arrow
import arrow

date = arrow.get('2020-01-18', 'YYYY-MM-DD')
print(date.shift(weeks=+6).format("MMM DD YYYY"))

import pandas

visitors = [1235, 6424, 9345, 8464, 2345]
errors = [23, 45, 33, 45, 76]
df = pandas.DataFrame({"visitors": visitors, "errors": errors}, index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)
print(df["errors"].mean())
print(df["visitors"].mean())