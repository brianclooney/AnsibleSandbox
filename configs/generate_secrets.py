#!/usr/bin/env python3

import argparse
from common import load_data, replace_secrets, save_data

def main():
    
    parser = argparse.ArgumentParser(description="Process and convert between JSON and YAML files.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("output_file", help="Output file path")
    args = parser.parse_args()

    data = load_data(args.input_file)
    data = replace_secrets(data)
    save_data(data, args.output_file)

if  __name__ == "__main__":
    main()
