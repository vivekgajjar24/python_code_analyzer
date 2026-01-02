Python Code Analyzer

Python Code Analyzer is a lightweight static analysis tool that scans a directory of Python files and provides basic insights into the code structure. It analyzes each file to count the total number of lines, functions, and classes using Python’s built-in Abstract Syntax Tree (AST).

Features

Scans folders recursively for .py files

Counts total lines of code

Detects number of functions and classes

Uses AST for accurate code parsing

Modular and easy-to-understand design

No external dependencies required

Tech Stack

Python 3.x

Built-in Libraries: ast, os

Project Structure
.
├── main.py
├── file_scanner.py
├── file_reader.py
├── parser.py
├── extractor.py
└── file_analyzer.py

Installation

Clone the repository:

git clone https://github.com/yourusername/python-code-analyzer.git
cd python-code-analyzer


Ensure Python is installed:

python --version

Usage

Open main.py

Update the directory path:

target_path = r"D:\Your\Python\Folder"


Run the program:

python main.py

Sample Output
Code Analyzer Started

Analyzing: example.py
   Lines     : 120
   Functions : 8
   Classes   : 2

How It Works

Scans the target directory for Python files

Reads and parses source code using AST

Extracts function and class definitions

Displays code metrics for each file

Use Cases

Understanding Python project structure

Learning static code analysis

Academic mini projects

Resume and portfolio projects

Future Enhancements

Variable and import analysis

Cyclomatic complexity calculation

Command-line arguments support

Export analysis reports
