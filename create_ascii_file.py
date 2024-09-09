# Create a text file with Unicode values for each character including letters with tilde
with open('unicode_values.txt', 'w', encoding='utf-8') as file:
    for i in range(32, 256):  # Unicode values from space (32) to 255
        file.write(f"{chr(i)}: {i}\n")