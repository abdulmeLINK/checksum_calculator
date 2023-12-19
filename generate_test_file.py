import os
import random
import string

# Define the minimum and maximum size of the file in bytes
min_size = 64
max_size = 1024

# Generate a random size between the minimum and maximum
size = random.randint(min_size, max_size)

# Generate a random string of the chosen size
content = ''.join(random.choices(string.ascii_letters + string.digits, k=size))

# Write the random string to a file
with open('test.txt', 'w') as f:
    f.write('god tells you: '+content)
