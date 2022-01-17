from prettytable import PrettyTable

table = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])

table.add_row(['Adelaide', 1295, 1158259, 600.5])
table.add_row(['Brisbane', 5905, 1857594, 1146.4])

table.align = "l"
print(table)
