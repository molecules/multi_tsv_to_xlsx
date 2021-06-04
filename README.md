# multi_tsv2xlsx

    usage: multi_tsv2xlsx_CLI [-h]
                                    [--remove-cols REMOVE_COLS [REMOVE_COLS ...]]
                                    [--delimiter DELIMITER]
                                    xlsx tsv_files [tsv_files ...]
    
    Create one xlsx file from multiple tab-separated-value files, with the option
    to remove columns.
    
    positional arguments:
      xlsx                  Name of xlsx file to create
      tsv_files             One or more tsv files to add to spreadsheet
    
    optional arguments:
      -h, --help            show this help message and exit
      --remove-cols REMOVE_COLS [REMOVE_COLS ...]
                            One or more tsv files to add to spreadsheet
      --delimiter DELIMITER
                            Delimiter for input files (default: tab character)


# multi_csv2xlsx
usage: multi_csv2xlsx [-h] [--remove-cols REMOVE_COLS [REMOVE_COLS ...]]
                      [--delimiter DELIMITER]
                      xlsx csv_files [csv_files ...]

Create one xlsx file from multiple comma-separated-value files, with the
option to remove columns.

positional arguments:
  xlsx                  Name of xlsx file to create
  csv_files             One or more csv files to add to spreadsheet

optional arguments:
  -h, --help            show this help message and exit
  --remove-cols REMOVE_COLS [REMOVE_COLS ...]
                        One or more csv files to add to spreadsheet
  --delimiter DELIMITER
                        Delimiter for input files (default: comma)

# Acknowledgemnets

Many thanks to the Pandas developers whose work does the heavy lifting for this script.

Thanks to EdChum from StackOverflow (for the index=False answer in this question:  https://stackoverflow.com/a/22089870/215487).

Thanks to stabledog from StackOverflow (for how to write multiple csv files to one spreadsheet: https://stackoverflow.com/revisions/42093077/4)

Thanks to https://www.askpython.com/python-modules/pandas/remove-column-from-python-dataframe for pointing the pop method for removing columns.
