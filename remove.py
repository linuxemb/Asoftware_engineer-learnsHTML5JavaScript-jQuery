# import re

# # Define a regular expression pattern to match timestamps
# timestamp_pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

# # Function to remove timestamps, split lines, and keep Chinese text
# def remove_timestamp_and_keep_chinese(input_file, output_file):
#     with open(input_file, 'r', encoding='utf-8') as f:
#         content = f.read()

#     # Remove timestamps and keep only Chinese text
#     chinese_text = re.sub(timestamp_pattern, '', content)
#     chinese_text = re.sub(r'[^\u4e00-\u9fff]', '', chinese_text)

#     # Split the lines
#     chinese_lines = chinese_text.split('.')

#     with open(output_file, 'w', encoding='utf-8') as f:
#         for line in chinese_lines:
#             # Remove leading and trailing whitespace from each line
#             line = line.strip()
#             if line:
#                 f.write(line + '\n')

# def main():
#     input_file = 'input.txt'  # Replace with the path to your input file
#     output_file = 'output.txt'  # Replace with the desired output file name

#     remove_timestamp_and_keep_chinese(input_file, output_file)

# if __name__ == '__main__':
#     main()

import re

# Define a regular expression pattern to match timestamps
timestamp_pattern = r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}'

# Function to remove timestamps and keep Chinese text
def remove_timestamp_and_keep_chinese(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    chinese_lines = []

    for line in lines:
        # Remove timestamps
        if re.match(timestamp_pattern, line):
            continue
        
        # Keep only Chinese text and non-empty lines
        chinese_text = re.sub(r'[^\u4e00-\u9fff]', '', line.strip())
        if chinese_text:
            chinese_lines.append(chinese_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(chinese_lines))

def main():
    input_file = 'input.txt'  # Replace with the path to your input file
    output_file = 'output.txt'  # Replace with the desired output file name

    remove_timestamp_and_keep_chinese(input_file, output_file)

if __name__ == '__main__':
    main()


