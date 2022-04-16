import time
import sys
import os

timestamp = time.strftime("# %Y-%m-%d %H:%M:%S")
line2 = "# Runtime "
line3 = "# Memory "
filename = sys.argv[1]

with open(filename, "w") as file:
    file.write("\n".join([timestamp, line2, line3]))

os.system(f"vi {filename}")
