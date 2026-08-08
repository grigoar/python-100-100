# ? Errors examples:

# file not found error


def file_not_found_error():
    try:
        with open("file.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found")
        file = open("file.txt", "w")
        file.write("Hello, world!")
        file.close()
    else:
        print("File found")
    finally:
        # raise FileNotFoundError("File not found!!!!!!")
        print("File closed")

    # type error


def type_error():
    try:
        print(1 + "1")
    except TypeError:
        print("Type error")


def main():
    file_not_found_error()
    type_error()


if __name__ == "__main__":
    main()

# The small set I'd learn first

# Coming from TypeScript, I'd start with these:

# Python	Rough TS/JS equivalent	Typical situation
# ValueError	RangeError / invalid value	Right type, bad value
# TypeError	TypeError	Wrong type/operation
# KeyError	accessing missing object key	dict["missing"]
# IndexError	array index error	arr[100]
# AttributeError	accessing missing property	obj.foo doesn't exist
# FileNotFoundError	filesystem error	File doesn't exist
# PermissionError	filesystem permission error	Can't access file
# ZeroDivisionError	RangeError-ish	Division by zero
# ImportError / ModuleNotFoundError	module resolution error	Import failed
# TimeoutError	timeout exception	Operation timed out
# NotImplementedError	similar	Deliberately unimplemented

value_errors = [
    "ValueError",
    "TypeError",
    "KeyError",
    "IndexError",
    "AttributeError",
    "FileNotFoundError",
    "PermissionError",
    "ZeroDivisionError",
    "ImportError",
    "ModuleNotFoundError",
]
