import pandas as pd
import csv
import argparse
from os import path as osp

def parser():
	
	# read in file name
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', nargs='+', default=[])

	args = parser.parse_args()
	FILE = args.file
	return FILE
	
def clean(FILE):

	df = pd.read_csv(FILE)
	path = osp.dirname(FILE)

	# Only keep relevant data (and drop all empty columns)
	df = df[['Date/Time', 'Year', 'Month', 'Day', 'Max Temp (°C)', 'Min Temp (°C)', 'Mean Temp (°C)', 'Total Precip (mm)', 'Spd of Max Gust (km/h)']]
	df.columns = ['Date', 'Year', 'Month', 'Day', 'Max Temp', 'Min Temp', 'Mean Temp', 'Total Precip (mm)', 'Spd of Max Gust (km/h)']

	# convert '<31' to float-interpretable value
	for index, row in df.iterrows():
		if df['Spd of Max Gust (km/h)'][index] == '<31':
			df['Spd of Max Gust (km/h)'][index] = '0.0'

	# Convert dtype to number and clean all nan's
	df = df.dropna(axis=0)
	cols =[i for i in df.columns if i not in ['Date']]
	for col in cols:
		df[col] = df[col].astype('float16')

	# Convert relevant columns to int type
	df[['Year', 'Month', 'Day', 'Spd of Max Gust (km/h)']] = df[['Year', 'Month', 'Day', 'Spd of Max Gust (km/h)']].astype('int16')

	# Save df as csv
	pd.DataFrame.to_csv(df, FILE, index=False)


def main():

	files = parser()

	print('files:', files)

	for file in files:
		print('Current file:', file)
		clean(file)

if __name__ == "__main__":
	main()
