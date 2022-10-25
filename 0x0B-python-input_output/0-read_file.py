def read_file(filename=""):
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')

#read_file("my.txt")