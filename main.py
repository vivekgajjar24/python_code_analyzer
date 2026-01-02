print("Code Analyzer Started")
from file_scanner import find_python_files
from file_analyzer import analyze_file

target_path=r"D:\Vivek\Inetrnship\BnB Tech\code-analyzer\__MACOSX\code-analyzer"
files = find_python_files(target_path)

for file in files:
    print(f"\nAnalyzing: {file}")

    result = analyze_file(file)

    print(f"   Lines     : {result['lines']}")
    print(f"   Functions : {result['functions']}")
    print(f"   Classes   : {result['classes']}")
