# from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).parent

# file = open(Path(__file__).parent / "my_file.txt")
# print(file.read())
# file.close()


# # write to a file
# file = open(Path(__file__).parent / "my_file.txt", "a")
# file.write("\ngggg!")
# file.close()

# # read from a file
# file = open(Path(__file__).parent / "my_file.txt")
# print(file.read())
# file.close()

# # delete a file

# with open(Path(__file__).parent / "my_file.txt") as file:
#     print(file.read())

# with open(Path(__file__).parent / "my_file.txt", "a") as file:
#     file.write("\nhhhhh!")

# with open(Path(__file__).parent / "my_file.txt") as file:
#     print(file.read())

# with open("../day24-files-directories-paths/my_file.txt") as file:
#     print(file.read())

PLACEHOLDER = "[name]"
# read the names from the invited_names.txt file and replace the [name] placeholder with the name from the list
with open(f"{BASE_DIR}/names/invited_names.txt") as file:
    names = file.readlines()

# replace the [name] placeholder with the name from the list
with open(f"{BASE_DIR}/letters/letter.txt") as file:
    letter = file.read()
for name in names:
    name = name.strip()
    with open(f"{BASE_DIR}/letters/letter_{name}.txt", "w") as file:
        file.write(letter.replace(PLACEHOLDER, name))

# read the names from the invited_names.txt file and replace the [name] placeholder with the name from the list
# save the letter to the letters directory
with open(f"{BASE_DIR}/letters/letter.txt") as file:
    letter = file.read()
    for name in names:
        name = name.strip()
        with open(f"{BASE_DIR}/letters/letter_{name}.txt", "w") as file:
            file.write(letter.replace(PLACEHOLDER, name))
