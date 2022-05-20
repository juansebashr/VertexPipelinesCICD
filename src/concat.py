import argparse
import pathlib
import os

parser = argparse.ArgumentParser(description='Concatenate text')
parser.add_argument('--param1',  type=str, help='The first text.')
parser.add_argument('--param2', type=str, help='The second text.')
parser.add_argument('--output_path', type=str, help='Path of the local file where the Output data should be written')
args = parser.parse_args()

print(args.param1)
print(args.param2)
print(args.output_path)

concat = args.param1 + args.param2

print(concat)

path = pathlib.PurePath(args.output_path)
os.makedirs(path.parent)

with open(args.output_path + '.txt', 'w') as f:
    f.write(concat)
