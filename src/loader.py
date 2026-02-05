from datetime import date, time
from pathlib import Path
import pandas as pd

#load csv
df = pd.read_csv(r'C:\Users\User\Desktop\panels_power_quality_project\Aggregate.csv')
df = df.iloc[::2]

#convert data and time columns to datetime.date and datetime.time, and combine
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Time'] = pd.to_datetime(df['Time'])
df['Timestamp'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str))
df = df.set_index('Timestamp', drop=False)
df = df.sort_index()

#drop irrelevant columns
df = df.drop(['VoltageN','CurrentN','THDN', 'Apparent Power1', 'Apparent Power2', 'Apparent Power3', 'Reactive Power1', 'Reactive Power2', 'Reactive Power3', 'Current1H13', 'Current2H13', 'Current3H13', 'Current1H15', 'Current2H15', 'Current3H15', 'CurrentNH1', 'CurrentNH3', 'CurrentNH5', 'CurrentNH7', 'CurrentNH9', 'CurrentNH11', 'CurrentNH13', 'CurrentNH15', 'Date', 'Time'], axis=1)

#export df
data_dir = Path('data')
file_path = data_dir / 'panel_aggregate.csv'
data_dir.mkdir(parents=True, exist_ok=True)
df.to_csv(file_path, index=False)

print(f"File successfully saved to: {file_path}")