import matplotlib.pyplot as plt
import csv
from datetime import datetime
from pathlib import Path

def get_rain_data(filename, dates_index, prcp_index):
    file_path = Path(filename)
    lines = file_path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[dates_index], '%Y-%m-%d')
        try:
            rain = float(row[prcp_index])
        except ValueError:
            print(f'Missing Data from {current_date}')
        else:
            dates.append(current_date)
            prcp.append(rain)
        
    return dates, prcp

dates, prcp = [], []
sitka_dates, sitka_rainfall = get_rain_data('weather_data/sitka_weather_2021_full.csv', 2, 5)

plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.plot(dates, prcp, c='blue')

dates, prcp = [], []
death_valley_dates, death_valley_rainfall = get_rain_data('weather_data/death_valley_2021_full.csv', 2, 3)

ax.plot(dates, prcp, c='red')

ax.set_title('Daily Rainfall 2021, \nSitka, AK and Death Valley, CA', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rainfall (in)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()