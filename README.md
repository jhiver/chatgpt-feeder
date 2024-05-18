# ChatGPT Feeder

## Overview

The ChatGPT Feeder script is a utility designed to prepare and copy large amounts of text from files into the clipboard for easy pasting into ChatGPT or other interfaces. This script recursively reads files from a specified directory, filters them based on specified include and exclude criteria, and then processes the contents in manageable chunks.

## Features

- **Recursive Directory Scanning**: Reads all files from the specified directory and its subdirectories.
- **File Filtering**: Includes files based on specified extensions and excludes directories based on specified names.
- **Chunked Copying**: Splits large amounts of text into manageable chunks and copies each chunk to the clipboard, pausing for user interaction between chunks.

## Usage

```sh
python chatgpt_feeder.py <directory> [-exclude_dir] [+include_ext] ...
```

### Parameters

- `<directory>`: The root directory to start scanning for files.
- `-exclude_dir`: A directory to exclude from scanning. Multiple exclude directories can be specified.
- `+include_ext`: A file extension to include in the processing. Multiple include extensions can be specified.

### Example

To process all `.ts` and `.js` files in `/path/to/dir` while excluding any `node_modules` directories, run:

```sh
python chatgpt_feeder.py /path/to/dir -node_modules +ts +js
```

### Detailed Steps

1. **Specify the Directory**:
   - Provide the root directory to start scanning for files.

2. **Include Filters**:
   - Use `+` followed by the file extension to specify which types of files to include (e.g., `+js` to include `.js` files).

3. **Exclude Filters**:
   - Use `-` followed by the directory name to specify which directories to exclude (e.g., `-node_modules` to exclude the `node_modules` directory).

4. **Run the Script**:
   - Execute the script with the specified parameters. The script will read the files, process the text into chunks, and copy each chunk to the clipboard.

5. **Interact with the Script**:
   - After each chunk is copied to the clipboard, the script will prompt you to press "Enter" to continue to the next chunk. This allows you to paste the content into your desired interface before proceeding.

## Example Output

```sh
$ python chatgpt_feeder.py /path/to/dir -node_modules +js +ts
chunk 1/4 copied to clipboard
Press Enter to continue to the next chunk...
chunk 2/4 copied to clipboard
Press Enter to continue to the next chunk...
chunk 3/4 copied to clipboard
Press Enter to continue to the next chunk...
chunk 4/4 copied to clipboard
Press Enter to continue to the next chunk...
```

## Dependencies

- Python 3.x
- `pyperclip` module

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install the `pyperclip` module:

```sh
pip install pyperclip
```

## License

This script is provided "as-is" without any warranties. Feel free to modify and use it as needed.
