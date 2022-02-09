import os
def main():
    with open("toolsNameList", "r") as toolsNameList:
        lines = toolsNameList.readlines()
        for line in lines:
            name = line.rstrip("\n")
            command = ("man {} > {}".format(name, name))
            os.system(command)

main()
