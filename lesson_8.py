import os
base = {}
new = {}
path = 'txt.txt'

with open(path) as f:
    for line in f:
        key,val = line.strip().split(':')
        base[key] = val.split()

new_key,new_val = list(map(str,input().strip().split(':')))
new[new_key] = new_val.split()
print(new_key)
for key,val in base.items():
  print(f"{key} : {' '.join(val)}")
f.close()
    
print ('newwww')
for key,val in list(base.items()):
    if key == new_key:
        del base[new_key]
        
base[new_key] = new_val.split()
print(base)
os.remove(path)

with open(path, 'w') as data:
    for key,val in base.items():

        data.write(str(key) + ':' + str(base[key]) + '\n')
        
    
data.close()

