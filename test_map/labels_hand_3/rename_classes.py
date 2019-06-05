#Copyright 2019 Oliver Struckmeier
#Licensed under the GNU General Public License, version 3.0. See LICENSE for details

from os import listdir

# This script was used because initially some classes in the label folders had wrong number representations
# Its not very flexeible but i decided to keep it around in case someone else
# needs to change the object class numbers after generating a dataset

labels_path = "/home/oli/Workspace/LeagueAI/test_map/labels_hand_3"

for i in listdir(labels_path):
    print(i)
    print(str(i.split(".")))
    if str(i.split(".")[1]) != "txt":
        print("skipping: ", i)
        continue

    with open(labels_path+"/"+i) as f:
        content = f.readlines()
    new_content = []
    for j in range(0, len(content)):
        cur_line = content[j]
        obj_class = cur_line.split(" ")[0]
        rest = [0] + cur_line.split(" ")[1:]
        print(obj_class)
        if int(obj_class) == 0:
            obj_class = 0
        elif int(obj_class) == 1:
            obj_class = 1
        elif int(obj_class) == 2:
            obj_class = 1
        elif int(obj_class) == 3:
            obj_class = 1
        elif int(obj_class) == 4:
            obj_class = 2
        print(obj_class)
        print("==")
        rest[0] = obj_class
        output_line = rest
        new_content.append(str(output_line[0]) + " " + str(output_line[1]) + " " + str(output_line[2]) + " " + str(output_line[3]) + " " + str(output_line[4]))
    with open(labels_path+"/"+i, "w") as f:
        f.writelines(new_content)

