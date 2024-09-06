# Define the number of rows
rows = 5

# Iterate over the rows
for i in range(rows):
    # Print the spaces for indentation
    print(' ' * (rows - i - 1), end='')
    # Print the asterisks (*)
    print('*' * (2 * i + 1))
