
tecnologiasbackend = ["\nPython", "\nRuby", "\nJava", "\nNode JS"]
file = open(
'c:/Users/kenndy/Desktop/python/clases_uni/clase_7/mi_file/file_4.txt',
"a+"
)

file.writelines(tecnologiasbackend)

file = open(
    "c:/Users/kenndy/Desktop/python/clases_uni/clase_7/mi_file/file_4.txt", "r"
    )

# fasfsda
"""
que loco
"""
for newline in file:
    if "python" in newline.lower():
        print("tienes en tu lista a python")
file.close()
