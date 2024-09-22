from parser import parse_args
from csv_utils import read_csv, compare_csv, check_df_size
from txt_utils import extract_patterns, compare_patterns, group_patterns_by_property


if __name__ == "__main__":
    base_file, compare_file, type, property_names = parse_args()
    if type == 'csv':
        base_df = read_csv(base_file, property_names)
        compare_df = read_csv(compare_file, property_names)
        compare_csv(base_df, compare_df, base_file, compare_file)
    if type == 'txt' and len(property_names) == 1:
        patterns_base_file = extract_patterns(base_file, property_names[0])
        patterns_compare_file = extract_patterns(compare_file, property_names[0])
        compare_patterns(patterns_base_file, patterns_compare_file)