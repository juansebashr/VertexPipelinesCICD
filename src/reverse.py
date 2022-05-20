import argparse
import pathlib
import os

parser = argparse.ArgumentParser(description='Training resusable components')
parser.add_argument('--input_path', type=str, help='The text to reverse.')
parser.add_argument('--output_path', type=str, help='Path of the local file where the Output data should be written')
args = parser.parse_args()

print(args.input_path)

with open(args.input_path  + '.txt', 'r') as input_file:
  input_string = input_file.read()

reversed_string = input_string[::-1]

path = pathlib.PurePath(args.output_path)
os.makedirs(path.parent)

with open(args.output_path  + '.txt', 'w') as ouput_file:
  ouput_file.write(reversed_string)
