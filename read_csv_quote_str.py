import csv

# https://stackoverflow.com/questions/43067373/split-by-comma-and-how-to-exclude-comma-from-quotes-in-split

line = '"this" "is very" "something csv" "values"'
lines = [line]
reader = csv.reader(lines, delimiter=' ', quotechar='"')
parsed_lines = [line for line in reader]
for parsed in parsed_lines:
    print(parsed)
