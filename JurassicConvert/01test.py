import json

s = json.loads('[{"Id":1,"Key":"params","Value":"","Pid":-1,"Children":[{"Id":2,"Key":"method","Value":"Post|Get","Pid":1,"Children":[]},{"Id":3,"Key":"filter","Value":"","Pid":1,"Children":[{"Id":4,"Key":"$and","Value":"","Pid":3,"Children":[{"Id":5,"Key":"bo:well","Value":"@bo:well","Pid":4,"Children":[]},{"Id":6,"Key":"it:pt","Value":"@it:pt","Pid":4,"Children":[]}]}]}]}]')

print(s)
