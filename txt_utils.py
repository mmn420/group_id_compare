from tabulate import tabulate
from collections import defaultdict

def extract_patterns(file_path, property_name):
    patterns = []
    current_pattern = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if ':' not in line:
                current_pattern = line
            elif property_name in line:
                class_id = line.split(':')[1]
                if current_pattern:
                    patterns.append((current_pattern, class_id))
                    current_pattern = None

    return patterns

def normalize_groups(grouped_patterns):
    return [set(pattern for pattern, class_id in group) for group in grouped_patterns.values()]

def group_patterns_by_property(patterns):
    grouped_patterns = defaultdict(list)
    for pattern, class_id in patterns:
        key = class_id 
        grouped_patterns[key].append((pattern, class_id))
    return grouped_patterns

def get_patterns_with_ids(groups, grouped_patterns):
    # Create a reverse mapping from pattern to class ID
    pattern_to_class_id = {}
    for class_id, patterns in grouped_patterns.items():
        for pattern, _ in patterns:
            pattern_to_class_id[pattern] = class_id

    # Collect patterns with their corresponding class IDs
    patterns_with_ids = defaultdict(list)
    for group in groups:
        for pattern in group:
            class_id = pattern_to_class_id.get(pattern)
            if class_id:
                patterns_with_ids[class_id].append(pattern)
    
    return patterns_with_ids

def format_patterns_with_ids(patterns_with_ids, compare_patterns_with_ids=None):
    formatted_patterns = []
    compare_class_id_map = {}
    
    if compare_patterns_with_ids:
        for comp_class_id, comp_patterns in compare_patterns_with_ids.items():
            for pattern in comp_patterns:
                compare_class_id_map[pattern] = comp_class_id

    for class_id, patterns in patterns_with_ids.items():
        compare_class_id = None
        if compare_patterns_with_ids:
            compare_class_id = next((compare_class_id_map[pattern] for pattern in patterns if pattern in compare_class_id_map), None)
        if not compare_class_id:
            formatted_patterns.append((class_id, ", ".join(patterns)))
        elif not patterns_with_ids:
            formatted_patterns.append((compare_class_id, ", ".join(patterns)))
        else:
            formatted_patterns.append((class_id, compare_class_id, ", ".join(patterns)))
    
    return formatted_patterns

def compare_patterns(patterns_file1, patterns_file2):
    grouped_patterns_file1 = group_patterns_by_property(patterns_file1)
    grouped_patterns_file2 = group_patterns_by_property(patterns_file2)

    normalized_groups1 = normalize_groups(grouped_patterns_file1)
    normalized_groups2 = normalize_groups(grouped_patterns_file2)

    common_groups = [group for group in normalized_groups1 if group in normalized_groups2]
    unique_to_file1 = [group for group in normalized_groups1 if group not in normalized_groups2]
    unique_to_file2 = [group for group in normalized_groups2 if group not in normalized_groups1]

    output = []

    if len(unique_to_file1) == 0 and len(unique_to_file2) == 0:
        output.append("All groups match between the files.")
        output.append("Common groups:")
        common_patterns_with_ids_file1 = get_patterns_with_ids(common_groups, grouped_patterns_file1)
        common_patterns_with_ids_file2 = get_patterns_with_ids(common_groups, grouped_patterns_file2)
        output.append(tabulate(format_patterns_with_ids(common_patterns_with_ids_file1, common_patterns_with_ids_file2), headers=["Group ID base_file", "Group ID compare_file", "Patterns"], tablefmt="grid"))
    else:
        output.append("Mismatching groups found.")
        output.append("\nMismatching Groups in base_file:")
        unique_to_file1_patterns_with_ids = get_patterns_with_ids(unique_to_file1, grouped_patterns_file1)
        output.append(tabulate(format_patterns_with_ids(unique_to_file1_patterns_with_ids), headers=["Group ID", "Patterns"], tablefmt="grid"))

        output.append("\nMismatching Groups in compare_file:")
        unique_to_file2_patterns_with_ids = get_patterns_with_ids(unique_to_file2, grouped_patterns_file2)
        output.append(tabulate(format_patterns_with_ids(unique_to_file2_patterns_with_ids), headers=["Group ID", "Patterns"], tablefmt="grid"))

    print("\n".join(output))
    exit(0 if len(unique_to_file1) == 0 and len(unique_to_file2) == 0 else 1)