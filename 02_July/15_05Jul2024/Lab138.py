# Standard lib pyhton which can help


import os
all_dir = os.listdir('/')
print(all_dir)

# Environment variable
print(os.environ.get('PATH'))

os.environ["saurbh"] = "saurabh"
print(os.environ.get('saurbh'))