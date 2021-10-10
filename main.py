# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import re
if __name__ == '__main__':

    f = open(sys.argv[1],'r')
    data = f.readline().split()
    print(int(data[0])+int(data[1]))









