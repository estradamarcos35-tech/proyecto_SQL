import pandas as pd

url = 'https://practicum-content.s3.us-west-1.amazonaws.com/data-analyst-eng/moved_chicago_weather_2017.html'

weather_records = pd.read_html(url, attrs={'id': 'weather_records'})[0]

weather_records.info()
print(weather_records)