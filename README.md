# cs31-checker

### Setup
This project assumes your project directory is located within this folder, and the source file is contained directly within the project directory (no subfolders)

### Installation and Execution
```shell
/ $ cd ~
~ $ git clone https://github.com/akhil99/cs31-checker.git
~ $ mv myProjectDirectory cs31-checker/
~ $ cd cs31-checker
~/cs31-checker/ $ sudo pip install yaml
~/cs31-checker/ $ ~ python verify.py config.yaml
```

### Config file template
```yaml
---
# Directory containing source cpp file
dir: AssignmentX

# (list) All files in directory
files:
    - file1.cpp
    - file2.txt

# (list) cpp files to test compile
compile:
    - file1.cpp

# compiler to use
compiler: clang++

# output template, where '~n' is replaced with the
# value out[n] for each test case
template: "s~0b~1\n~2"

# test cases
tests:
-   file: keyboard # binary file to test (no extension)
    in: '\n' # string to pass to program, read by cin
    out: ['0', '0',''] # values to insert into template
```
