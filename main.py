# Phone Book App - Command Line

import pickle

records_file = "phonebook.pickle"
records = {}
s = ""

try:
    f = open(records_file, 'r')
    records = pickle.load(f)
    f.close()
    print "Phonebook records found and loaded."
except IOError:
    print "No phonebook records found."

already_count = 0
border = "\n" + "="*60 + "\n"
doubleborder = "\n" + "="*60 + border

options = [
"1 - Look up an entry",
"2 - Set an entry",
"3 - Delete an entry",
"4 - List all entries",
"5 - Quit"
]

def pBorder(s):
    print border + s.center(60) + border

def pHeader(s):
    print doubleborder + s.center(60) + doubleborder

def returnToMenu():
    s = str(raw_input("Enter 'y' to return to the menu: "))
    menu()

def lookup(caller):
    global s, already_count
    header = "LOOKUP"
    pHeader(header)
    pBorder("Who do you want to look up?")
    s = str(raw_input("Name: "))
    if s in records.keys():
        current = records[s]
        l = "%s :: %s"%(s,current)
        pBorder(l)
        print "\n"
        print "Returning to menu\n\n\n"
    else:
        print border + "That entry does not exist.".center(60)
        print "Do you want to create a new entry for that name? (y/n)".center(60) + border
        s2 = str(raw_input())
        if s2 == "y":
            set_entry("lookup")
    returnToMenu()

def set_entry(caller):
    global s, already_count
    header = "SET ENTRY"
    if caller == "lookup":
        l = "What is %s's phone number? (xxx xxx-xxxx)" % s
        pBorder(l)
        e = str(raw_input())
        records[s] = e
        l = "The entry for %s has been saved as %s" % (s,records[s])
        pBorder(l)
    if caller == "menu":
        pHeader(header)
        pBorder("Who do you want to create an entry for?")
        name = str(raw_input("Name: "))
        l = "What is %s's phone number?" % name
        pBorder(l)
        number = str(raw_input("xxx xxx-xxxx : "))
        records[name] = number
        l = "The entry for %s has been saved as %s" % (name,records[name])
        pBorder(l)
    returnToMenu()

def delete(caller):
    global s, already_count, records
    header = "DELETE ENTRY"
    pHeader(header)
    pBorder("Who do you want to delete the entry for?")
    name = str(raw_input("Name: "))
    l = "The entry for %s is currently %s" % (name,records[name])
    pBorder(l)
    pBorder("Are you sure that you want to delete this record?")
    s = str(raw_input("(y/n): "))
    if s == "y":
        del records[name]
    returnToMenu()

def listall(caller):
    global s, already_count, records
    header = "LIST ALL ENTRIES"
    pHeader(header)
    for key,value in records.items():
        l = "%s :: %s"%(key,value)
        pBorder(l)
    returnToMenu()

def menu():
    global already_count, records_file, border, records, s
    header = "MENU"
    pHeader(header)
    for i in options:
        print i
    pBorder("What do you want to do? (1-5)")
    s = int(raw_input())
    if s < 5:
        caller = "menu"
        if s == 1:
            lookup(caller)
        elif s == 2:
            set_entry(caller)
        elif s == 3:
            delete(caller)
        else:
            listall(caller)
    else:
        pBorder("Are you sure you want to quit? (y/n)")
        s = str(raw_input())
        already_count += 1
        if s == "n":
            menu()
        already_count -= 1
        if already_count == 0:
            pBorder("Do you want to save your progess? (y/n)")
            s = str(raw_input())
            if s == "y":
                f = open(records_file, 'w')
                pickle.dump(records,f)
                f.close()
            print border + "Closing the program...".center(60)
            print "Goodbye!".center(60) + border

menu()
