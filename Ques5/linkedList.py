# WAP to assist the students in maintaining the results of each often experiment.
# The data will be stored in memory. With the use of Linked List, with List for data entry.
# Each entry will be processed in logged csv file. That contains following info.
# 1. Name of CSV file
# 2. The no. of lines in CSV file
# 3. Exp. rutime in ms
# 4. The experiment memoryu usage in bytes
# The list should be in Alphabetically Sorted order
# The program should be menu driven

from time import perf_counter

list_of_linked_lists = []


class Node:
    def __init__(self, name=None, line=None, sno=None, result=None, runtime=None, space=None):
        self.name = name
        self.data = line
        self.sno = sno
        self.result = result
        self.runtime = runtime
        self.space = space
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, node, pos=None):
        trav = self.head
        if (pos):
            for i in range(pos-2):
                trav = trav.next
            node.next = trav.next
            trav.next = node

        elif (pos == None):
            if (self.head == None):
                self.head = node
            else:
                while (trav.next != None):
                    trav = trav.next
                trav.next = node

    def insert_beg(self, node):
        node.next = self.head
        self.head = node

    def print_linked_list(self):
        trav = self.head
        print("Sno\tName\tLines\tSpace\tRuntime")
        while (trav):
            print(trav.sno, "\t", trav.name, "\t",
                  trav.data, "\t", trav.space, "\t", trav.runtime)
            trav = trav.next


def get_files():
    from os import listdir
    files = []
    # get files from data folder
    for file in listdir("data"):
        if file.endswith(".csv") and file != "results.csv":
            files.append(file)
    return files


def get_data_from_csv(fileName):
    from csv import reader
    with open(fileName, "r") as f:
        reader = reader(f)
        data = []
        for row in reader:
            data.append(row)
    return data


if __name__ == "__main__":
    from os import path, remove
    print("Welcome to the Linked List Program")
    if path.exists("results.csv"):
        remove("results.csv")

    while True:
        print("1. Add a new file")
        print("2. Print all the file names")
        print("3. Print all the data")
        print("4. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            linked_list = LinkedList()
            file_name = input("Enter the file name: ")
            data = get_data_from_csv("data/" + file_name)
            size = path.getsize("data/" + file_name)
            start = perf_counter()
            for i in range(len(data)):
                node = Node(name=file_name, line=i, sno=data[i][0],
                            result=data[i][1], runtime=(perf_counter() - start)*1000, space=size)
                linked_list.insert(node)
            end = perf_counter()
            print("File added successfully")
            print("Time taken: ", end - start)
            list_of_linked_lists.append(linked_list)
        elif ch == 2:
            print("File names are: ")
            for file in get_files():
                print(file)
        elif ch == 3:
            file_name = input("Enter the file name: ")
            for linked_list in list_of_linked_lists:
                if linked_list.head.name == file_name:
                    linked_list.print_linked_list()
        elif ch == 4:
            # Before exiting, write the data to the results.csv file
            with open("data/results.csv", "w") as f:
                from csv import writer
                w = writer(f)
                w.writerow(["Sno", "Name", "Lines", "Space", "Runtime"])
                for linked_list in list_of_linked_lists:
                    trav = linked_list.head
                    while (trav):
                        w.writerow([trav.sno, trav.name,
                                    trav.data, trav.space, trav.runtime])
                        trav = trav.next
            print("Thank you for using the program")
            break
        else:
            print("Wrong choice")
