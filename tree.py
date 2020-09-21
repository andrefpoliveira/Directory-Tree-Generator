import os, sys

def generateTree(path):
    tree = path + "\n"

    for root, _, files in os.walk(path):
        root = root.replace(path, "")
        level = root.count(os.sep)

        if level == 0:
            for file in files:
                tree += "  " * level + "|--" + file + "\n"

        else:
            tree += "|" + "--" * level + root + "\n"
            for file in files:
                tree += "|" + "  " * level + "|--" + file + "\n"

    print(tree)


if __name__=='__main__':
    if len(sys.argv) != 2:
        print("ERROR: Wrong number of arguments!")
        print("Usage: python3 tree.py <path>")
    elif not os.path.exists(sys.argv[1]):
        print("ERROR: That path doesn't exist!")
        print("Please provide a valid path")
    else:
        generateTree(sys.argv[1])