from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["#", "blox fruits name", "blox fruit types"]
# table.add_row(["1", "Dough", "mythical"])
# table.add_row(["2","Trex","mythical"])
# table.add_row(["3","portal","legendary"])
# table.add_row(["4","Buddha","legendary"])
# table.add_row(["5","light","rare"])
# table.add_row(["6","magma","rare"])
# table.add_row(["7","flame","uncommon"])
# table.add_row(["8","ice","uncommon"])
# table.add_row(["9","chop","common"])
# table.add_row(["10","smoke","common"])
# table.align = "l"

from prettytable import from_csv

with open("fruits.csv") as fruits:
     table = from_csv(fruits)
print(table)
