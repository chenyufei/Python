# -*- coding:utf-8 -*-
import os

deveui = "4a770065"
print(deveui.split("4a77")[1])
fd = open("upgrade_success_2019-12-11-17-15-42.txt")
login = fd.read()
print(len(login.split("4a77")))

fd = open("upgrade_success_2019-12-12-10-46-41.txt")
login = fd.read()
succ = login.split("4a77")
for dev in succ:
    if len(dev) != 0:
        # pass
        print("4a77"+dev)

print("")
print(len(succ))
