#DOWNLOADED THE PACKAGE PRETTY TABLE
from prettytable import PrettyTable

table=PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

print(table)
#output
'''
+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+
'''
table.align="l"

print(table)
#OUTPUT
'''
+--------------+----------+
| Pokemon Name | Type     |
+--------------+----------+
| Pikachu      | Electric |
| Squirtle     | Water    |
| Charmander   | Fire     |
+--------------+----------+
'''