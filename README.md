# AT2-182-CSV-Reader
Initial WIP for the csv reader for SKA OET configuration and duration file

How to use:
The Python file, json files and csv file needs to be used in conjunction with the cdm-shared-library: 
https://github.com/ska-telescope/cdm-shared-library.git

The files of this AT2-182-CSV-Reader repository should be placed in the same directory as the cdm-shared-library.
To Run. At the terminal in the cdm-shared-library directory type in python3 csv_reader.py

02/07/2019
----------
Currently the json to obj convertion does not work as expected.  It is though this is due to incorrect structuring of the data being
passed to the cdm_library function.
