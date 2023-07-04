def compare_text_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

        if len(text1) != len(text2):
            print("Error: Text files must have the same length.")
            return

#        comparison = [' ' if c1 == c2 else '^' for c1, c2 in zip(text1, text2)]
        comparison = [c1 if c1 == c2 else '-' for c1, c2 in zip(text1, text2)]
               
        print("Comparison Result:")
        print(''.join(comparison))


import sys

# Check if filename is provided as a command-line argument
if len(sys.argv) < 3:
    print("Please provide the 2 filenames of the same length as a command-line argument.")
    sys.exit(1)

filename1 = sys.argv[1]
filename2 = sys.argv[2]

compare_text_files(filename1, filename2)
