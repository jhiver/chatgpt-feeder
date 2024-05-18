#!/usr/bin/env python
import os
import sys
import uuid
import pyperclip

START_TOKEN = uuid.uuid4().hex
END_TOKEN = uuid.uuid4().hex

INITIAL_PROMPT = f"""
All subsequent messages are for context only. The context will be included
between start token {START_TOKEN} and end token {END_TOKEN}. You will just
answer 'OK' to acknowledge you received the text until you see the message
{END_TOKEN}.

{START_TOKEN}
"""

FINAL_PROMPT = f"""
{END_TOKEN}

The context has been sent. Now ask the user what they want to do, and
help them with their request the best you can.
"""

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='ISO-8859-1') as file:
            return file.read()

def split_text(text, chunk_size=15000):
    chunks = []
    while len(text) > chunk_size:
        chunk, text = text[:chunk_size], text[chunk_size:]
        chunks.append(chunk)
    chunks.append(text)
    return chunks

def get_all_files(directory, include_extensions, exclude_dirs):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        if any(exclude in root for exclude in exclude_dirs):
            continue
        for file in files:
            if any(file.endswith(ext) for ext in include_extensions):
                file_paths.append(os.path.join(root, file))
    return file_paths

def main():
    if len(sys.argv) < 3:
        print("Usage: python chatgpt_feeder.py <directory> [-exclude_dir] [+include_ext] ...")
        sys.exit(1)

    directory = sys.argv[1]
    include_extensions = []
    exclude_dirs = []

    for arg in sys.argv[2:]:
        if arg.startswith('+'):
            include_extensions.append(arg[1:])
        elif arg.startswith('-'):
            exclude_dirs.append(arg[1:])

    if not os.path.isdir(directory):
        print(f"Directory not found: {directory}")
        sys.exit(1)

    file_paths = get_all_files(directory, include_extensions, exclude_dirs)

    if not file_paths:
        print("No files found with the specified filters in the directory.")
        sys.exit(1)

    data = []
    data.append(INITIAL_PROMPT)
    
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        data.append(f"File: {file_path} START")
        data.append(read_file(file_path))
        data.append(f"File: {file_path} END")

    text = '\n'.join(data)
    chunks = split_text(text)
    i = 1
    length = len(chunks)
    for chunk in chunks:
        print(f"chunk {i}/{length} copied to clipboard")
        if i == length:
            pyperclip.copy(chunk + "\n" + FINAL_PROMPT)
        else:
            pyperclip.copy(chunk)
        input("Press Enter to continue to the next chunk...")
        i += 1

if __name__ == "__main__":
    main()
