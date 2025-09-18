# Build combined index for all parts of the data safety guidance and insert into the parts.

from typing import List
from pathlib import Path
from subprocess import run
import os
import sys

"""
Manage the overall process of building indexes.
"""
def build_indexes(base_directory: str) -> None:
    # The files that contain a \makeindex command which will need to be disabled on final pass
    makeindex_files: List[str] = [r'Source\dsiwgTemplate.tex']
    # The files that contain definitions for \docname which will need to be amended on final pass
    docname_files: List[str] = [r'Source\Part1\Part1.tex', r'Source\Part2\Part2.tex', r'Source\Part3\Part3.tex']
    # The main LaTeX source files
    source_files: List[str] = [r'Source\Part1\Part1.tex', r'Source\Part2\Part2.tex', r'Source\Part3\Part3.tex']
    index_files: List[List[str]] = [[r'Source\Part1\Part1.idx', r'Source\Part2\Part2.idx', r'Source\Part3\Part3.idx'], [r'Source\Part1\locationidx.idx', r'Source\Part3\locationidx.idx', r'Source\Part3\locationidx.idx', ]]

    compile_files(base_directory, source_files)
    make_glossaries(base_directory, source_files)
    
"""
Compile all the source LaTeX files.

Args:
    base_directory (str) the base directory for the doxument
    source_files (List) the files to be compiled.
Raise:
    OSError if file system operations fail
"""
def compile_files(base_directory: str, source_files: list[str]) -> None:
    for file in source_files:
        source_path = Path(file)
        source_directory: str = source_path.parent
        os.chdir(source_directory)
        result = run(f'pdflatex {source_path.name}')
        if result.returncode != 0:
            sys.stderr.write(f'Failed to build LaTeX file')
            sys.exit(1)
        os.chdir(base_directory)
        

"""
Make the glossaries.

Args:
    base_directory (str) the base directory for the doxument
    source_files (List) the files for the glossaries.
Raise:
    OSError if file system operations fail
"""
def make_glossaries(base_directory:str, source_files: list[str]) -> None:
    for file in source_files:
        source_path = Path(file)
        source_directory: str = source_path.parent
        try:
            os.chdir(source_directory)
        except OSError as e:
            sys.stderr.write(f'Failed to enter working directory. {e.strerror}')
            raise e
        run(f'makeglossaries {source_path.stem}')
        try:
            os.chdir(base_directory)
        except OSError as e:
            sys.stderr.write(f'Failed to enter base directory. {e.strerror}')
            raise e

def concatenate_indexes(base_directory:str, index_files: list[str]) -> None:


if __name__ == "__main__":
    try:
        base_directory:str = os.getcwd()
    except OSError as e:
        sys.stderr.write(f'Failed to get current working directory. {e.strerror}')
        raise e    
    build_indexes(base_directory)
