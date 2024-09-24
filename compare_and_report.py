from tabulate import tabulate

def compare_groups(dict1, dict2):
    all_groups_match = True
    mismatch_groups = []
    for sets, groups in dict1.items():
        dict1_group = dict2.get(sets)
        if dict1_group is None:
            all_groups_match = False
            mismatch_groups.append([groups, ', '.join(map(str, sets))])
    return all_groups_match, mismatch_groups



def report_group_comparison(base_sets_to_groups, compare_sets_to_groups, group_column, ID_column):
    all_base_group_match , mismatch_groups_base = compare_groups(base_sets_to_groups, compare_sets_to_groups)
    all_compare_group_match , mismatch_groups_compare = compare_groups(compare_sets_to_groups, base_sets_to_groups)
    if all_base_group_match and all_compare_group_match:
        print("All groups match between the files.")
        table_data = [
            [base_sets_to_groups[group], compare_sets_to_groups.get(group, "N/A"), ', '.join(map(str, group))]
            for group in base_sets_to_groups.keys()
        ]
        print(tabulate(table_data, headers=[f"base_file {group_column}", f"compare_file {group_column}", f"{ID_column}"], tablefmt="grid"))
        exit(0)
    else:
        print("Mismatching groups found.")
        if mismatch_groups_base:
            print("Mismatching groups from base_file:")
            print(tabulate(mismatch_groups_base, headers=[f"base_file {group_column}", f"{ID_column}"], tablefmt="grid"))
        if mismatch_groups_compare:
            print("Mismatching groups from compare_file:")
            print(tabulate(mismatch_groups_compare, headers=[f"compare_file {group_column}", f"{ID_column}"], tablefmt="grid"))
        exit(1)