# The `find` command

- What does `find . -name '*.csv'` do?
    - **Answer**: recursively searches for anything with a name that ends in ".csv" under the current directory

- What does `find foo/ -name 'bar'` do?
    - **Answer**: recursively searches for things named "bar" (exactly) under the directory "foo"

- Your current directory contains a file named "test_backend.py". Will `find . -name 'test'` match it?
    - **Answer**: No, it only matches things named exactly "test"

- What is the difference between `-name` and `-iname` in the `find` command?
    - **Answer**: `-iname` is case-insensitive, while `-name` is case-sensitive.

- What does `find . -type d -name 'data*'` do?
    - **Answer**: Finds directories (not files) whose names start with "data".

- What does `find . -name 'test' -maxdepth 1` do?
    - **Answer**: Finds things named "test" in the current directory, but does not search subdirectories.

- What does `find . -name '*.csv' -exec rm {} \;` do?
    - **Answer**: deletes all CSVs under the current directory and its subdirectories

- In `find . -name '*.csv' -exec rm {} \;`, what does `{}` represent?
    - **Answer**: a placeholder that gets replaced with the path of each found file

- What does `find . -type f -name '*.py' -exec grep 'foo' {} \;` do?
    - **Answer**: Prints every line containing "foo" in every `.py` file in this directory and its subdirectories.

# The `grep` command

- What does `grep foo bar` do?
    - **Answer**: searches for the string "foo" in the file "bar" and prints matching lines

- What does `grep foo .` do?
    - **Answer**: Prints an error, because without `-r`, grep expects a file, not a directory.

- What does `grep -r foo bar` do?
    - **Answer**: searches for the string "foo" in all files under the directory "bar" recursively

- What does `grep -ri foo bar` do?
    - **Answer**: searches for the string "foo" in all files under the directory "bar" recursively, ignoring case

- What does `grep -n foo bar` do?
    - **Answer**: searches for the string "foo" in the file "bar" and prints matching lines, prefixed with their line number

- The file `file.txt` contains the line "One foo bar two". Will `grep 'foo' file.txt` return (match) that line?
    - **Answer**: Yes, it matches because "foo" is a substring of "One foo bar two"

- The file `file.txt` contains the line "ONE FOO BAR TWO". Will `grep 'foo' file.txt` return (match) that line?
    - **Answer**: No, it does not match because grep is case-sensitive
