#!/usr/bin/env python3

import argparse
from common import find_yaml_files, merge_yaml_files, save_data

def main():

    parser = argparse.ArgumentParser(description="Process and convert between JSON and YAML files.")
    parser.add_argument("-d", "--dir", dest="roles_dir", default="roles", help="Path to the directory containing Ansible roles (optional).")
    parser.add_argument("output_file", help="Output file name or '-' for stdout")
    args = parser.parse_args()

    yaml_files = list(find_yaml_files(args.roles_dir))
    data = merge_yaml_files(yaml_files)
    save_data(data, args.output_file)

if  __name__ == "__main__":
    main()
