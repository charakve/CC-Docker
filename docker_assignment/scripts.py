import os
import string
from collections import Counter
import contractions
import socket

import re

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

# Get IP address of the container
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

file_content_1 = read_file("/home/data/IF.txt")
file_content_2 = read_file("/home/data/AlwaysRememberUsThisWay.txt")

# Fix Contractions
file_content_1 = contractions.fix(file_content_1)
file_content_2 = contractions.fix(file_content_2)


# Remove punctuation, replace dashes with spaces, and replace newlines with spaces
file_content_1 = file_content_1.translate(str.maketrans('', '', string.punctuation)).replace("—", " ").replace("-", " ").replace("\n", " ")
file_content_2 = file_content_2.translate(str.maketrans('', '', string.punctuation)).replace("—", " ").replace("-", " ").replace("\n", " ")

# Split into words directly
list_1 = file_content_1.split()
list_2 = file_content_2.split()

# Function to get the top N frequent words
def top_words(word_list, ignore_list=[], top_n=1):
    word_count = Counter(word.lower() for word in word_list if word.lower() not in ignore_list)
    return word_count.most_common(top_n)

# Get the top 3 most frequent words of IF.txt
top_1 = top_words(list_1, [])
top_2 = top_words(list_1, [top_1[0][0]], top_n=1)
top_3 = top_words(list_1, [top_1[0][0], top_2[0][0]], top_n=1)

top_words_1 = f"Top 3 words in IF.txt: {top_1[0]}, {top_2[0]}, {top_3[0]}"

# Get the top 3 most frequent words of AlwaysRememberUsThisWay.txt
top_1 = top_words(list_2, [])
top_2 = top_words(list_2, [top_1[0][0]], top_n=1)
top_3 = top_words(list_2, [top_1[0][0], top_2[0][0]], top_n=1)

top_words_2 = f"Top 3 words in AlwaysRememberUsThisWay.txt: {top_1[0]}, {top_2[0]}, {top_3[0]}"

# Get IP address
ip_address = get_ip_address()


result = f"""
    IF.txt word count: {len(list_1)}
    AlwaysRememberUsThisWay.txt word count: {len(list_2)}
    Total word count: {len(list_2) + len(list_1)}
    {top_words_1}
    {top_words_2}
    Container IP Address: {ip_address}
"""

output_file = '/home/data/output/result.txt'

os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, 'w') as f:
    f.write(result)

output = read_file("/home/data/output/result.txt")
print(output)

