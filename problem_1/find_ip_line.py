import sys;


fp  = open("ip_lines.txt", "r")

lines = fp.readlines();

count = 0
for line in lines:
    if(line.split("\n")[0] == sys.argv[1]):
            count = count+1

if count == 0:
    print("ip not found")
else:
    print("ip was found ", count, "times")

fp.close()
