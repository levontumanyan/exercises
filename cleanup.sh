#!/bin/bash

# Check if argument is a directory
if [[ ! -d $1 ]]; then
    echo "Error: Argument is not a directory"
    exit 1
fi

# Delete binary files without an extension and print the list of deleted files
find $1 -type f ! -name "*.*" ! -path "*/.git/*" -print | while read file; do
    if [[ $(file --mime-encoding "$file") != *ascii* ]]; then
        echo "$file"
        rm -f "$file"
    fi
done

find $1 -name "*.dSYM" -type d -prune -print -exec rm -rf {} +
