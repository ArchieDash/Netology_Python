import csv

flats_list = list()

with open('output.csv', newline='') as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=';')
    flats_list = list(flats_csv)

# TODO 1:
for i, flat in enumerate(flats_list):
    if "новостройка" in flat:
        print("-\n{0}\nID:{1}\nAdress:{2}\nPrice:{3} RUR\nWed-link:{4}".format(i, flat[0], flat[6], flat[11], flat[19]))
        print("\n\n")

    # TODO 2:
flats_intersesction = set(flats_list[2]) & set(flats_list[5])
print(flats_intersesction, "\t", type(flats_intersesction), "\n")
print(set(flats_list[0]) & set(flats_list[len(flats_list) - 1]))
print(set(flats_list[120]) & set(flats_list[200]))
print(set(flats_list[11]) & set(flats_list[111]) & set(flats_list[101]))
print("\n\n")

# TODO3:
test_dict = dict()
for i, flat in enumerate(flats_list):
    if i == 0:
        continue
    test_dict[flat[19]] = flat[0]
print(test_dict)
print(type(test_dict))