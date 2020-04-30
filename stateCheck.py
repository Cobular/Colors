file = open("colors.txt","r")
fileLength = len(file.readlines)

def check_state():
    with open("colorsWritten.txt","r") as file2:
        print("State: {}% complete!".format(len(file2.readlines)/fileLength))