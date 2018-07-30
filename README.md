# A python3 CLI utility to interface with [pastething](https://github.com/lbatalha/pastething)

Example: https://cpy.pt

## Dependencies

* python3
* requests

## Installation

Using pip is the easiest way to install this
Install from pypi: `pip install capyt`

You can also manually install this from source:
* install dependencies - `pip install -r requirements.txt`
* symlink `capyt/capyt.py` to a location of your choice
* adjust defaults and options if required

## Usage

`capyt -h` to see all available options

### Pasting

- paste a single file `capyt somefile`
- create a single paste with many files concatenated `capyt file1 file2 file3`
- paste from stdin `somestdout | capyt -`

### Deleting a paste

- `capyt -d DELETE_TOKEN PASTE_ID`
- `capyt -d DELETE_TOKEN https://cpy.pt/PASTE_ID`

## Extra Features

* Transparently open gzip and bzip compressed files

## Warning

The optional encoding flag only serves to open the file, internally everything is handled and converted to utf-8.
Retrieved pastes are utf-8 encoded.
