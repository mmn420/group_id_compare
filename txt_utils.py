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
                grouping_property_id = line.split(':')[1]
                if current_pattern:
                    patterns.append((current_pattern, grouping_property_id))
                    current_pattern = None
    return patterns

def group_patterns(patterns):
    grouped_patterns = defaultdict(list)
    for pattern, grouping_property_id in patterns:
        key = grouping_property_id 
        grouped_patterns[key].append((pattern, grouping_property_id))
    return grouped_patterns
def group_and_normalize_patterns(patterns):
    grouped_patterns = group_patterns(patterns)
    normalized_dict = {}
    for group in grouped_patterns.keys():
        pattern_set = frozenset(pattern for pattern, group in grouped_patterns[group])
        normalized_dict[pattern_set] = group
    return normalized_dict