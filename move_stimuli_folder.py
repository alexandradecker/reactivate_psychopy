import os
import shutil
import csv

i = 0
for i in list(range(287)):
    with open('to_extract_images.csv', newline='') as csvfile:
        to_move_file = csv.reader(csvfile, delimiter=',')
        for row in to_move_file:
            name = row[i]
            os.rename('images/' + name, 'images_new/' + name)
            print(name + " moved to new folder.")