#!/usr/bin/env python3
import csv
import json
import os
import shutil
import sys
from zipfile import ZipFile

import openpyxl
import pandas

src_datasets_dir = "././datasets"
list_of_datasets_zip_files = ["oil-prices.zip", "population.zip", "ppp.zip"]
dest_datasets_dir = "././data/"


def main():
    print_version()
    remove_dst()
    unpack_archive()
    copy_csv_files()
    read_csv()
    convert_csv_to_json_and_xlsx()


def print_version():
    print(sys.version)


def remove_dst():
    if dest_datasets_dir and dest_datasets_dir not in ('/', './'):
        shutil.rmtree(dest_datasets_dir, ignore_errors=True)


def unpack_archive():
    for dataset_zip_file in list_of_datasets_zip_files:
        zip_full_path = os.path.join(src_datasets_dir, dataset_zip_file)
        with ZipFile(zip_full_path, 'r') as zip_obj:
            zip_obj.extractall(dest_datasets_dir)


def copy_csv_files():
    if os.path.exists('././src') == False:
        os.mkdir('././src')
        paths_from = ['././data/oil-prices-master/data', '././data/population-master/data/', '././data/ppp-master/data/']
        paths_to = ['././src/oil-prices', '././src/population', '././src/ppp']

        for i in range(len(paths_from)):
            os.mkdir(paths_to[i])
            k = 0
            for file in os.listdir(paths_from[i]):
                if '.csv' not in file:
                    continue
                k += 1
                path_join = os.path.join(paths_from[i], file)
                shutil.copy2(path_join, paths_to[i])


def read_csv():
    paths_to = ['././src/oil-prices', '././src/population', '././src/ppp']
    for i in range(len(paths_to)):
        k = 0
        for file in os.listdir(paths_to[i]):
            if '.csv' not in file:
                continue
            k += 1
            path_join = os.path.join(paths_to[i], file)
            data_list = read_csv_list(path_join)
            data_dict = read_csv_dict(path_join)


def read_csv_list(filename):
    lines = []
    with open(filename, 'r') as data:
        for line in csv.reader(data):
            lines.append(line)
    return lines


def read_csv_dict(filename):
    with open(filename, 'r') as f:
        dict_reader = csv.DictReader(f)
        list_of_dict = list(dict_reader)
    return list_of_dict


def convert_csv_to_json_and_xlsx():
    paths_to = ['././src/oil-prices', '././src/population', '././src/ppp']
    for i in range(len(paths_to)):
        k = 0
        for file in os.listdir(paths_to[i]):
            if '.csv' not in file:
                continue
            k += 1
            path_join = os.path.join(paths_to[i], file)
            data_json, filename_json = convert_csv_to_json(path_join)
            filename_xlsx = convert_json_to_xlsx_by_pandas(filename_json)


def convert_csv_to_json(path_join):
    data = read_csv_dict(path_join)
    dn_json = os.path.dirname(path_join)
    fn_csv_name = os.path.basename(path_join)
    fn_parts = os.path.splitext(fn_csv_name)
    fn_name = fn_parts[0]
    filename_json = os.path.join(dn_json, fn_name + '.json')
    data_json = json.dumps(data, indent=2)

    with open(filename_json, "w") as json_file:
        json_file.write(data_json)

    return data_json, filename_json


def convert_json_to_xlsx_by_pandas(filename_json):
    fn_parts = os.path.splitext(filename_json)
    fn_name = fn_parts[0]
    filename_xlsx = fn_name + '_pandas.xlsx'
    pandas.read_json(filename_json).to_excel(filename_xlsx, index=False)

    return filename_xlsx


if __name__ == '__main__':
    main()

