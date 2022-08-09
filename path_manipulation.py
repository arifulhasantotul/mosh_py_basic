from pathlib import Path

# path.exists() return True or False
"""
path = Path("ecommerce_pack")
print(path.exists())
"""
# path.mkdir(name) creates a folder/path according to name
"""
createPath = Path("emails")
createPath.mkdir()
"""
# path.rmdir(name) removes a folder/path matched the name
"""
removePath = Path("emails")
removePath.rmdir()
"""

# path.glob(str) returns all the matched files.
# str = "*.*" then return all files
# str = "*.py" then return all python files
# str = "loop.py" then return only loop.py file
# str = "*.xlsx" then return all xlsx files
# str = "*.docx" then return all docx files

search_files = Path()
for file in search_files.glob("*.py"):
    print(file)
