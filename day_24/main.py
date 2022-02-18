with open("Input/names.txt", "r") as f:
    names = f.readlines()

with open("Input/starting.txt", "r") as f:
    values = f.read()


for name in names:
    values = values.replace("[name]", name.strip())
    with open(f"Output/letter_for_{name.strip()}.txt", "w") as f:
        f.write(values)
