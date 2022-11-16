#!/usr/bin/python3
# randomBook.py
import random
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

def main():
    num = input("Type '1' if you want to create a new list of books from the MD file and choose a random book or Type '2' if you want to see a random book from the current toRead.txt file \n")

    url = "http://github.com/rlivingsus/misc/blob/main/AllBooks.md"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    
    if num == "1":
        os.system('rm toRead.txt')
        fd = open('colon.txt','w')
        fd.write(soup.get_text())
        colon = ':'
        with open('colon.txt','r') as fp:
            #read all lines in file
            lines = fp.readlines()
            for line in lines:
                if colon in line:
                    fi = open('toRead.txt','a')
                    fi.write(line)
            fi.close()
        line = random.choice(open('toRead.txt').readlines())
        print(line)
    elif num == "2":
        line = random.choice(open('toRead.txt').readlines())
        print(line)

if __name__ == '__main__':
    main()
