def myFile(filename):
    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"file {filename} is not found")

myFile("1.txt")
myFile("2.txt")
myFile("3.txt")