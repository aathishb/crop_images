import sys
from PIL import Image

if (len(sys.argv) < 2):
    print("Usage: python crop.py filenames")
    sys.exit()

pos_names = ["left", "top", "right", "bottom"]
pos = [0, 0, 0, 0]

for i in range (0, 4):
    while True:
        try:
            val = int(input("Enter " + pos_names[i] +
                            " pixel crop position: "))
        except ValueError:
            print("Enter an integer number.")
            continue
        else:
            if (val < 0):
                print(pos_names[i] + " crop position cannot be negative\n")
                continue
            else:
                if (i < 2):
                    pos[i] = val
                    break
                else:
                    if (val <= pos[i-2]):
                        print(pos_names[i] + " crop position must be greater than " +
                              pos_names[i-2] + " position\n")
                        continue
                    else:
                        pos[i] = val
                        break
        
for i in range (1, len(sys.argv)):
    im = Image.open(sys.argv[i])
    
    left = pos[0]
    top = pos[1]
    right = pos[2]
    bottom = pos[3]
    im = im.crop( (left, top, right, bottom) )
    
    name = sys.argv[i];
    offset = len(sys.argv[i])-4;
    name = sys.argv[i][:offset] + "-00" + sys.argv[i][offset:]
    im.save(name)
