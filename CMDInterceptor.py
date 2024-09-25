import sys, subprocess

# directories that intercetped commands should ask confirmation for before modifying
protected_dirs = [
    "/",
    "~",
    "test"
]

# sys.argv[i] example structure:
#         [0]       [1] [2] [3]
# python  Sh-16.py  rm  -rf  /

# check if command will modify any protected_dirs
warned = False
for i in range(2, len(sys.argv)):
    if sys.argv[i][0] == "-":
        # just a command argument
        continue
    elif sys.argv[i] in protected_dirs:
        while True: 
            x = input("This looks like a dangerous command. Are you sure you want to execute? [N/y]: ")
            if x == "" or x == "N" or x == "n":
                break
            elif x == "Y" or x == "y":
                subprocess.run(sys.argv[1:])
                break
        warned = True
        break

if not warned:
    # didn't trigger any warnings; most likely safe
    subprocess.run(sys.argv[1:])

