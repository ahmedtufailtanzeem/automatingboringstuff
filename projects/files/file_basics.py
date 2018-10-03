import os

print(os.getcwd())
os.chdir(os.path.join('/Users', 'tanz'))
print(os.getcwd())