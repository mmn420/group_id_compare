# Group ID Compare

This project provides a script to compare groups of IDs from CSV or TXT files and generate a report on the comparison.

## Installation

Install the required dependencies:
```sh
pip install -r requirements.txt
```

## Usage

To run the script, use the following command:
```sh
python group_id_compare.py <base_file> <compare_file> <type> <property_names>
```
# Generate TXT Patterns
``./Tests/txt/generate_txt_pattern.py `` is used to generate a txt file in the following pattern:
```
Pattern1
Size:43.84
Class_id:11
Pattern2
Size:25.52
Class_id:78
Pattern3
Size:64.56
Class_id:4
Pattern4
.......
```
you can use it by running the following command in the terminal
```
cd ./Tests/txt
python generate_txt_pattern.py <number_of_patterns>
```
# Run all Test Scenarios
## For CSV files
```sh
python ./group_id_compare.py -base_file ./Tests/csv/Mismatching_groups/file1.csv -compare_file ./Tests/csv/Mismatching_groups/file2.csv -type csv -property DefectID cluster_ID 

python ./group_id_compare.py -base_file ./Tests/csv/Matching_groups/With_different_group_ids/file1.csv -compare_file ./Tests/csv/Matching_groups/With_different_group_ids/file2.csv -type csv -property DefectID cluster_ID 

python ./group_id_compare.py -base_file ./Tests/csv/Matching_groups/With_same_group_ids/file1.csv -compare_file ./Tests/csv/Matching_groups/With_same_group_ids/file2.csv -type csv -property DefectID cluster_ID 
```

## For txt files
```sh
python ./group_id_compare.py -base_file ./Tests/txt/Mismatching_groups/file1.txt -compare_file ./Tests/txt/Mismatching_groups/file2.txt -type txt -property Class_id 

python ./group_id_compare.py -base_file ./Tests/txt/Matching_groups/With_different_group_ids/file1.txt -compare_file ./Tests/txt/Matching_groups/With_different_group_ids/file2.txt -type txt -property Class_id 

python ./group_id_compare.py -base_file ./Tests/txt/Matching_groups/With_same_group_ids/file1.txt -compare_file ./Tests/txt/Matching_groups/With_same_group_ids/file2.txt -type txt -property Class_id 

```
