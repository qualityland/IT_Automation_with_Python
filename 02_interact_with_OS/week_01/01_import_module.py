# cli installation:
# pip install arrow
import arrow

date = arrow.get('2020-01-18', 'YYYY-MM-DD')
print(date.shift(weeks=+6).format("MMM DD YYYY"))