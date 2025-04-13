# Check Plagiarism Script

Script used to check plagiarism using the Dolos API.

## Features

- Creates a ZIP file from the specified text file.
- Sends the ZIP file to the Dolos API.
- Gets the plagiarism report URL in HTML format.

## Prerequisites

Make sure you have the following libraries installed:
- `requests`
- `zipfile` (part of Python standard library)
- `os` (part of Python standard library)

To install `requests`, use the following command:
```bash
pip install requests
```

## How to Use

- Enter the text you want to scan into the text.txt file
- Then, run the program using the following command:
```bash
python plag.py
```

## Notes

- The Dolos API requires a ZIP file for the submission process.
- Make sure the text file you want to check already exists and its path is correct.
- The report URL will be returned if the process is successful.
