with open("file1.txt", "r") as file:
    content1 = file.readlines()

with open("file2.txt", "r") as file:
    content2 = file.readlines()

def find_variance(list1, list2):
    unmatching = []
    for i in list1:
        if i not in list2:
            unmatching.append(i)
    return unmatching

def show_variance(unique_list):
    if unique_list:
        for i in unique_list:
            print(i, end = '')
        print("")
    else:
        print("All strings match")

print("Unique strings from the first file:")
show_variance(find_variance(content1, content2))
print("----------------------------------------")
print("Unique strings from the second file:")
show_variance(find_variance(content2, content1))
print("----------------------------------------")
print("What happens if we compare the file with itself:")
show_variance(find_variance(content1, content1))



