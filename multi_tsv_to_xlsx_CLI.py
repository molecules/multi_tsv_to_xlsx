#!/cluster/biocompute/software/python/python-3.7.6/bin/python
# multi_tsv_to_xlsx_CLI.py
"""
Create one xlsx file from multiple tab-separated-value files, with the option to remove columns.
"""

import argparse
import pandas as pd
import os
from pathlib import Path


def main(args):

    if Path(args.xlsx).is_file():
        print(f'Cowardly refusing to overwrite "{args.xlsx}". Exiting now.')
        exit()

    if not os.path.splitext(args.xlsx)[-1] == '.xlsx':
        print('Exiting because output spreadsheet name "{args.xlsx}" does '
              'not end in ".xlsx".'
              )

    # Create an Excel XLSX file writing object, using the first filename from the command line
    writer = pd.ExcelWriter(args.xlsx)

    # Create a sheet for each TSV file
    for tsv_file in args.tsv_files:
        df = pd.read_csv(tsv_file, sep=args.delimiter)  # read in delimited file

        if args.remove_cols:
            for column in args.remove_cols:
                df.pop(str(column))  # remove specified column

        # Write out current file as sheet
        df.to_excel(
            writer,
            # sheet has same name as file (without the extension)
            sheet_name=os.path.splitext(tsv_file)[0],
            index=False                               # prevent column of row numbers
        )

    # Save and close final xlsx file containing one or more sheets
    writer.save()


# command line interface (making this a modulino)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument(
        'xlsx',
        type=str,
        help='Name of xlsx file to create',
    )
    parser.add_argument(
        'tsv_files',
        nargs='+',
        type=str,
        help='One or more tsv files to add to spreadsheet',
    )
    parser.add_argument(
        '--remove-cols',
        nargs='+',
        type=str,
        help='One or more tsv files to add to spreadsheet',
    )
    parser.add_argument(
        '--delimiter',
        type=str,
        default="\t",
        help='Delimiter for input files',
    )

    # Capture the command line arguments
    args = parser.parse_args()

    # pass command line arguments to the main function
    main(args)
