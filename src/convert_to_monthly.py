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

def convert(FILE):

    df = pd.read_csv(FILE)
    path = osp.dirname(FILE)
    file_name = osp.basename(FILE)

	# Decided to not look at gust speeds
    if 'Spd of Max Gust (km/h)' in df.columns:
	       df = df.drop('Spd of Max Gust (km/h)', axis=1)

    # Columns we want in final def
    columns = ['Date', 'Year', 'Month', 'Max Temp', 'Min Temp', 'Mean Temp', 'Total Precip (mm)']

    # Define dict to populate
    my_dict = {}

    for col in columns:
        my_dict[col] = []

    # Populate dict with all mean values from df
    for month in df['Month'].unique():
        my_dict['Date'].append(str(int(df[df['Month'] == month]['Year'].mean())) + '-' + str(month).zfill(2))
        my_dict['Year'].append(str(int(df[df['Month'] == month]['Year'].mean())))
        my_dict['Month'].append(str(month))
        my_dict['Max Temp'].append(df[df['Month'] == month]['Max Temp'].mean())
        my_dict['Min Temp'].append(df[df['Month'] == month]['Min Temp'].mean())
        my_dict['Mean Temp'].append(df[df['Month'] == month]['Mean Temp'].mean())
        my_dict['Total Precip (mm)'].append(df[df['Month'] == month]['Total Precip (mm)'].mean())

    new_df = pd.DataFrame.from_dict(my_dict)
    new_df.columns = columns

	# Save df as csv
    pd.DataFrame.to_csv(new_df, osp.join(path, '..', str('monthly_' + file_name)), index=False)

def main():

    files = parser()

    print('files:', files)

    for file in files:
        print('Current file:', file)
        convert(file)

    print('Finished with:', file)

if __name__ == "__main__":
	main()
