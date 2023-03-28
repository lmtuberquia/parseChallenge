"""
    This script is designed to parse the input file and transform its content according to the ReplaceSentence class.
    The script then creates an instance of ReplaceSentence class and calls its 'replace' method to transform the content of the input file.
    The transformed sentence is then printed to the console.

The script uses argparse module to allow for command line argument parsing. The required argument is the input file to be processed.

Usage: 
    python script_name.py --f input_file.txt

Arguments:
    --file, -f: Required. Specifies the input file to be processed.

Class used:
    - ReplaceSentence

Dependencies:
    - argparse module
    - parsentence module

"""


import argparse
from parsentence import ReplaceSentence

parser = argparse.ArgumentParser(description='Process input file')

parser.add_argument('--file', '-f', type=str, required=True,
                    help='input file to be processed')

if __name__ == '__main__':
    args = parser.parse_args()
    input_file = args.file

    replace_sentence = ReplaceSentence()

    with open(input_file, 'r') as myfile:
        file_content = myfile.read()

    transformed_sentence = replace_sentence.replace(file_content)
    print(transformed_sentence)
