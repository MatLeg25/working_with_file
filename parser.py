import sys #importuje komendy systemowe

'''
if len(sys.argv) >= 2:
    name = sys.argv[1]
    print(f"Hello {name} !!!")
else:
    print(" [WARNING] You should run this program by calling: pyton parser.py your_name")

#print(sys.argv)
'''

filename = "input.txt"

def get_filename():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        return filename
    else:
        print(" [WARNING] You should run this program by calling: pyton parser.py your_name")
        return ""

def main():
    file = get_filename()
    if len(filename) == 0:
        return

    print(f"File to parse: {filename}")



if __name__ =="__main__":   #main odpali sie tylko gdy ktos odpali ten konkretny plik a nie podczas importu w innym miejscu ?
    main()
