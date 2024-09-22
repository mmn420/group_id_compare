import argparse
import os
def parse_args():
    parser = argparse.ArgumentParser(description='Compare two files based on given properties.')
    parser.add_argument('-base_file', required=True, help='The base file to compare.')
    parser.add_argument('-compare_file', required=True, help='The file to compare against the base file.')
    parser.add_argument('-type', required=True, choices=['txt', 'csv'], help='The type of the files (txt or csv).')
    parser.add_argument('-property_names', required=True, nargs='+', help='The property names to compare.')

    args = parser.parse_args()

    base_file = args.base_file
    compare_file = args.compare_file
    files_type = args.type
    property_names = args.property_names

    if not os.path.exists(base_file):
        print(f'Error: The base file "{base_file}" does not exist.')
        exit(1)
    if not os.path.exists(compare_file):
        print(f'Error: The compare file "{compare_file}" does not exist.')
        exit(1)
    if files_type not in ['txt', 'csv']:
        print(f'Error: The type "{files_type}" is not supported.')
        exit(1)
    if files_type == 'txt' and len(property_names) != 1:
        print(f'Error: The type "{files_type}" requires exactly one property name (The grouping_id).')
        exit(1)
    return base_file, compare_file, files_type, property_names