
def compare_files(file1, file2, output_file1, output_file2):
    # Read lines from both files and strip whitespace
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines_file1 = {line.strip() for line in f1}
        lines_file2 = {line.strip() for line in f2}

    # Lines unique to file1 and file2
    lines_unique_to_file1 = lines_file1 - lines_file2
    lines_unique_to_file2 = lines_file2 - lines_file1

    # Write unique lines to output files
    with open(output_file1, 'w') as out1, open(output_file2, 'w') as out2:
        out1.write('\n'.join(lines_unique_to_file1))
        out2.write('\n'.join(lines_unique_to_file2))


if __name__ == '__main__':
  compare_files('file1.txt', 'file2.txt', 'output1.txt', 'output2.txt')
