# multi_tsv_to_xlsx

    usage: multi_tsv_to_xlsx_CLI.py [-h]
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
                            Delimiter for input files
