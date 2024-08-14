import os

# Specify the directory where your files are located
directory = '/home/kinnan/Downloads/legal/case_pdfs'

# Specify the prefix you want to add to the fil

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Construct the old file path
    old_file = os.path.join(directory, filename)

    # Skip directories
    if os.path.isfile(old_file):
        # Construct the new file name with the prefix
        new_file = os.path.join(directory, filename.replace('_1.pdf', '.pdf'))

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {old_file} to {new_file}')

print("Renaming complete.")
