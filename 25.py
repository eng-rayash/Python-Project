with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")


with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.strip())