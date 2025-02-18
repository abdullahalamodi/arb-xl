import argparse
from pathlib import Path
from arb_xl.json_to_xls import json_to_xls
from arb_xl.xls_to_json import xls_to_json

def main():
    parser = argparse.ArgumentParser(
    description="arb-xl: Convert JSON/ARB translation files to Excel and vice versa."
    )

    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # JSON to XLS command
    json_to_xls_parser = subparsers.add_parser(
        "j2x", 
        help="Convert JSON/ARB files to an Excel file."
    )
    json_to_xls_parser.add_argument("output_xls", type=Path, help="Path to save the output Excel file (e.g., output.xlsx).")
    json_to_xls_parser.add_argument("json_files", type=Path, nargs='+', help="JSON/ARB translation files to convert (e.g., en.json/arb ar.json/arb).")
    
    # XLS to JSON command
    xls_to_json_parser = subparsers.add_parser(
        "x2j", 
        help="Convert an Excel file back to JSON/ARB files."
    )
    xls_to_json_parser.add_argument("xls_file", type=Path, help="Excel file to convert (e.g., translations.xlsx).")
    xls_to_json_parser.add_argument("output_dir", type=Path, help="Directory to save the JSON/ARB files (e.g., trasnlations/).")
    xls_to_json_parser.add_argument("--arb", action="store_true", help="Convert to .arb format instead of .json.")
    
    args = parser.parse_args()
    
    if args.command == "j2x":
        print(f"Converting JSON/ARB files {args.json_files} to {args.output_xls}...")
        json_to_xls(args.json_files, args.output_xls)
    elif args.command == "x2j":
        print(f"Converting {args.xls_file} to {'ARB' if args.arb else 'JSON'} files in {args.output_dir}...")
        xls_to_json(args.xls_file, args.output_dir,use_arb=args.arb)
        

if __name__ == "__main__":
    main()
