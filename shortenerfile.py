import os
path = 'test_truncate.txt'
# creating the file
fp = open(path, 'w')
fp.write('truncate data string')
fp.close()
# cut it
os.truncate(path, 8)
fp = open(path, 'r')
print(fp.read())
# `truncate`
fp.close()
# clean
os.unlink(path)