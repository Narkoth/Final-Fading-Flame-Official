# A script to aid in the editing of the definition.csv file in a Hoi4 Mod
# By Narkoth 

import csv
import io

def edit_the_file(p_id, terrain_type):
    all_lines = []
    with open("definition.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            all_lines.append(', '.join(row))
    with open("definition.csv", "w", newline='') as csvfile:
        c = ";"
        for line in all_lines:
            old_line = line.split(";")
            if (int(old_line[0]) == int(p_id)):
                new_line = [(p_id), (old_line[1]), (old_line[2]), (old_line[3]), (old_line[4]),  (old_line[5]),  (terrain_type), old_line[7]]
                spamwriter = csv.writer(csvfile, delimiter=';')
                spamwriter.writerow(new_line)
            else:
                old_row = [(old_line[0]), (old_line[1]), (old_line[2]), (old_line[3]), (old_line[4]),  (old_line[5]),  (old_line[6]), old_line[7]]
                spamwriter = csv.writer(csvfile, delimiter=';')
                spamwriter.writerow(old_row)

def main():
    print("Welcome to the definition.csv editor, because this stuff takes too long to do manually ...")
    keep_going = True
    while(keep_going == True):
        print("To continue, give the province ID number you wish to edit, OR, enter 'X' to quit: ")
        province_id = str(input())
        if(province_id == "X"):
            keep_going = False
            break
        else:
            print("Enter what terrain type you want to change it to: ")
            terrain = str(input())
            edit_the_file(province_id, terrain)
    
                
                
            
            
        
