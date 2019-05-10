import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
# for i in names_1:    1.35 secs
#     if i in names_2:
#         duplicates.append(i)
# duplicates = [i for i in names_1 if i in names_2]   1.29 secs possible stretch solution using Lists for storing of the names

duplicates = set(names_1).intersection(names_2) # .00399 secs sets use dictonaries so this solution can't be used for stretch

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

