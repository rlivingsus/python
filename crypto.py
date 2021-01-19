#!/usr/bin/python3
#REF: https://www.programiz.com/python-programming/methods/string/format
#REF: https://note.nkmk.me/en/python-bin-oct-hex-int-format/ 
#REF: https://www.binaryhexconverter.com/ 

import argparse

bi = "BIN"
he = "HEX"
oc = "OCT"
de = "DEC"

parser = argparse.ArgumentParser(description="Convert a Numeral to another Numeric type")
parser.add_argument("cvrtFrom", help="Convert Numeric type FROM...BIN, HEX, OCT, or DEC")
#parser.add_argument("cvrtTo", help="Convert Numeric type TO...BINARY, HEX, OCTAL, or DECIMAL")
parser.add_argument("numericValue", type=str, help="Numeral") 

args = parser.parse_args()    #parsing the arguments a
#print("converting from...", args.cvrtFrom)
#print("numericValue...", args.numericValue)
#print(type(args.numericValue))   #printing the "type" of numeric Value

def conDec(value):  
    print ("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(value))

def conBin(value):  
    integer = int(value, 2)           # this is valid and WORKS
    hexa = format(integer, 'x')       # use the newly converted int to convert to hex
    octal = format(integer, 'o')       # use the newly converted int to convert to octal
    print ("conBIN int value", integer, "oct value", octal, "hexa value", hexa)

def conHex(value):   
    integer = int(value, 16)    #finally figured out this int function works.  The value received is a string and you're converting value in second argument (here, it's a hex) to an integer
    bina = format(integer, 'b')
    octal = format(integer, 'o')
    print ("conHEX int value", integer, "oct value", octal, "binary value", bina)

def conOct(value):
    integer = int(value, 8)
    hexa = format(integer, 'x')
    bina = format(integer, 'b')
    print ("conOCT int value", integer, "hex value", hexa, "binary value", bina)

if __name__ == '__main__':   #I could change this to sending values to one function and checking the "args.cvrtFrom.lower()" within that one function and move these if statements and remove the other functions
    if args.cvrtFrom.lower() == bi.lower():
        #print ("convert args.numericValue from binary")
        conBin(args.numericValue)
    elif args.cvrtFrom.lower() == he.lower():
        #print ("convert args.numericValue from hex")
        conHex(args.numericValue)
    elif args.cvrtFrom.lower() == de.lower():
        #print ("convert args.numericValue from decimal")
        integer = int(args.numericValue)        #value is string so convert to integer then shoot to function
        conDec(integer)
    elif args.cvrtFrom.lower() == oc.lower():
        #print ("convert args.numericValue from oct")
        conOct(args.numericValue)
else:
    print ("test2")

    