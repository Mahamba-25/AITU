import os
path = r"C:\Users\Mahamba\Desktop"
dir_list = os.listdir(path)

txt_files = []
others = []

for I in dir_list:
    if os.path.isfile(os.path.join(path, I)):
        if I.endswith(".txt"):
            txt_files.append(I)
        else:
            others.append(I)

print(".txt files:\n")
print(txt_files)
print("\nOther files:\n")
print(others)
