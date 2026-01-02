from file_reader import read_file
from parser import parse_code
from extractor import extract_functions
import ast

def analyze_file(file_path):
    code = read_file(file_path)
    tree = parse_code(code)

    lines = len(code.splitlines())

    functions = extract_functions(tree)

    classes = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef)
    ]

    return {
        "file": file_path,
        "lines": lines,
        "functions": len(functions),
        "classes": len(classes)
    }
