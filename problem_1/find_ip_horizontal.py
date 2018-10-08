import sys;


fp  = open("ip_horizontal.txt", "r")

lines = fp.read();

line_list = lines.split(" ")

line_list[-1] = line_list[-1].split("\n")[0]

count = 0
for line in line_list:
    if(line == sys.argv[1]):
            count = count+1

if count == 0:
    print("ip not found")
else:
    print("ip was found ", count, "times")

fp.close()

