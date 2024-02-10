# Accepting Arguments from CLI
import argparse

parser = argparse.ArgumentParser(description="Example program for arguments")

parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow'}, help='the color to search for')

args = parser.parse_args()
print(args.color)