
""" WFQ assignment, that reads a text files, strips the names from the file and sorts them into
    their appropriate lists. It then prints the names out from each list a specified number of
    times until each list is empty."""

first_class = [] #list for premium
premium_economy = [] #list for standard
cattle_class = [] #list for economy

def input_sort():
    """ Functions allowing the opening and reading of a .txt file. As it reads the file
        it looks at the first character of each line and adds the proceeding name to an
        associating list."""
    with open("input queue-1.txt") as file:
        #print(file.read())
        for line in file:
            if line[0] == "P":
                first_class.append(line[2:].strip())
            elif line[0] == "S":
                premium_economy.append(line[2:].strip())
            else:
                cattle_class.append(line[2:].strip())
    #print(first_class)
    #print(premium_economy)
    #print(cattle_class)

def queue_processing(p,s,e):
    """ Function that takes the previously sorted lists and prioritizes the printing output of that list.
        it does this by using a for loop to iterate through a specified number items in each list.
        Then it pops the item off the list and prints it out. The loops are all nested in a while loop,
        so this process continues until all lists are empty."""
    while p or s or e:
        for n in range(3):
            if p:
                print("Premium: ",p.pop(0))
        for n in range(2):
            if s:
                print("Standard: ",s.pop(0))
        if e:
            print("Economy: ",e.pop(0))


if __name__ == "__main__":
    input_sort()
    queue_processing(first_class,premium_economy,cattle_class)
