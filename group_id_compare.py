from parser import parse_args
from csv_utils import read_csv, group_csv, check_df_size
from compare_and_report import report_group_comparison
from txt_utils import extract_patterns, group_and_normalize_patterns


if __name__ == "__main__":
    base_file, compare_file, type, property_names = parse_args()
    if type == 'csv':
        base_df = read_csv(base_file, property_names)
        compare_df = read_csv(compare_file, property_names)
        check_df_size(base_df, compare_df, base_file, compare_file)
        base_sets_to_groups, compare_sets_to_groups, group_column, ID_column = group_csv(base_df, compare_df)
        report_group_comparison(base_sets_to_groups, compare_sets_to_groups, group_column, ID_column)

    if type == 'txt' and len(property_names) == 1:
        patterns_base_file = extract_patterns(base_file, property_names[0])
        patterns_compare_file = extract_patterns(compare_file, property_names[0])
        grouped_patterns_base = group_and_normalize_patterns(patterns_base_file)
        grouped_patterns_compare = group_and_normalize_patterns(patterns_compare_file)
        report_group_comparison(grouped_patterns_base, grouped_patterns_compare, property_names[0], 'Patterns')
