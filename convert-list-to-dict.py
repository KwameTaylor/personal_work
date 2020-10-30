# Python3 program to Convert a 
# list to dictionary
 
import json
import pandas as pd

noun_list = [
    ["sar", "git"],
    ["sar", "github"],
    ["sar", "gitlab"],
    ["sar", "gitea"],
    ["sar", "bitbucket"],
    ["smer", "branch"],
    ["smer", "commit"],
    ["smber", "log"],
    ["smar", "pull request"],
    ["smar", "merge request"],
    ["smber", "stash"],
    ["sber", "status"],
    ["smber", "tag"],
    ["smber", "origin"],
    ["smber", "master"],
    ["smber", "lemur"],
    ["sber", "spacehuhn"],
    ["smber", "laser"],
    ["smber", "signal"],
    ["smber", "network"],
    ["smber", "analyzer"],
    ["smber", "application"],
    ["smber", "firewall"],
    ["smber", "cybernuke"],
    ["sber", "IRC"],
    ["smber", "mainframe"],
    ["smber", "server"],
    ["smber", "cloud"],
    ["smbr", "reality"],
    ["smer", "request"],
    ["sber", "WiFi"],
    ["sber", "Bluetooth"],
    ["smber", "cable"],
    ["sber", "ethernet"],
    ["sber", "LAN"],
    ["sber", "WAN"],
    ["smber", "antenna"],
    ["sber", "NAS"],
    ["smar", "power supply"],
    ["smber", "grid"],
    ["smber", "display"],
    ["smber", "monitor"],
    ["smber", "microcontroller"],
    ["smber", "controller"],
    ["ser", "SoC"],
    ["sbr", "SBC"],
    ["sbr", "ATX"],
    ["sbr", "ITX"],
    ["sbr", "USB"],
    ["ser", "HDD"],
    ["ser", "SSD"],
    ["smber", "keyboard"],
    ["smer", "transition"],
    ["smber", "tree"],
    ["ser", "SD"],
    ["ser", "LED"],
    ["ser", "IDE"],
    ["smer", "editor"],
    ["smer", "frame"],
    ["ser", "PoC"],
    ["smber", "bucket"],
    ["sber", "VM"],
    ["smer", "identifier"],
    ["sber", "middleware"],
    ["sber", "bottleneck"],
    ["ser", "UI"],
    ["ser", "GUI"],
    ["smber", "observer"],
    ["smber", "singleton"],
    ["smber", "array"],
    ["smber", "transmitter"],
    ["smber", "DVD"],
    ["ber", "logic"],
    ["smber", "emulation"],
    ["smer", "reader"],
    ["smer", "writer"],
    ["smer", "label"],
    ["smber", "clock"],
    ["smber", "MCU"],
    ["smber", "phone"],
    ["smber", "space"],
    ["sber", "data"],
    ["sber", "analysis"],
    ["smber", "sample"],
    ["sber", "intelligence"],
    ["smber", "sensor"],
    ["smber", "camera"],
    ["smber", "battery"],
    ["smber", "process"],
    ["smber", "website"],
    ["smber", "homepage"],
    ["smber", "app"],
    ["smber", "error"],
    ["smber", "warning"],
    ["smber", "sequence"],
    ["smber", "information"],
    ["sbr", "ASCII"],
    ["smber", "pattern"],
    ["smber", "simulation"],
    ["smber", "simulator"],
    ["sber", "indicator"],
    ["smber", "troll"],
    ["smber", "regulator"],
    ["smber", "container"],
    ["smber", "breadboard"],
    ["sber", "IC"],
    ["smber", "controller"],
    ["smber", "drone"],
    ["smber", "deauther"],
    ["smar", "if loop"],
    ["sar", "GTFO"],
    ["sber", "fax"],
    ["smar", "garbage collector"],
    ["smer", "collector"],
    ["smber", "thread"],
    ["smber", "model"],
    ["smber", "switch"],
    ["smber", "dimension"],
    ["sber", "foo"],
    ["sber", "bar"],
    ["smber", "key"],
    ["smber", "java"],
    ["smber", "coffee"],
    ["sbr", "null"],
    ["sbr", "NaN"],
    ["sbr", "undefined"],
    ["smber", "integer"],
    ["smber", "double"],
    ["smber", "string"],
    ["sar", "bare metal"],
    ["smber", "adapter"],
    ["smber", "framework"],
    ["smber", "system"],
    ["smber", "algorithm"],
    ["sbr", "spacetime"],
    ["smbr", "LCD"],
    ["sber", "bandwidth"],
    ["smber", "virus"],
    ["sbr", "UTF-8"],
    ["sber", "web"],
    ["sbr", "handler"],
    ["smber", "exeption"],
    ["smber", "path"],
    ["smber", "reference"],
    ["smber", "template"],
    ["smber", "wildcard"],
    ["smber", "interface"],
    ["sber", "syntax"],
    ["smber", "loop"],
    ["smber", "demon"],
    ["smber", "core"],
    ["sber", "interpreter"],
    ["smber", "string"],
    ["smber", "document"],
    ["smber", "cookie"],
    ["smber", "codec"],
    ["smber", "e-mail"],
    ["sber", "OS"],
    ["smber", "service"],
    ["sber", "provider"],
    ["smber", "cache"],
    ["smber", "database"],
    ["smber", "object"],
    ["smbers", "dictionary"],
    ["sber", "driver"],
    ["smber", "index"],
    ["sber", "encoder"],
    ["smber", "list"],
    ["smber", "tuple"],
    ["smber", "range"],
    ["smber", "stream"],
    ["sber", "internet"],
    ["smber", "component"],
    ["smber", "module"],
    ["smber", "library"],
    ["smber", "limit"],
    ["smber", "function"],
    ["smer", "token"],
    ["smber", "code"],
    ["smber", "wave"],
    ["sber", "IoT"],
    ["smber", "blockchain"],
    ["smber", "repository"],
    ["smber", "northbridge"],
    ["smber", "southbridge"]
]

'''
noun_list = pd.DataFrame(noun_list, axis=0)
noun_list = noun_list.set_index([0])
noun_list = noun_list.to_dict()
print(noun_list)
'''

'''
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
         
# Driver code
#lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(noun_list))
'''

'''
# Python3 code to demonstrate working of  
# Convert Lists of List to Dictionary 
# Using dictionary comprehension 
  
# initializing list 
#test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]] 
  
# printing original list 
print("The original list is : " + str(noun_list)) 
  
# Convert Lists of List to Dictionary 
# Using dictionary comprehension 
res = {tuple(sub[:1]): tuple(sub[1:]) for sub in noun_list} 
      
# printing result  
print("The mapped Dictionary : " + str(res))  
'''

'''
dict = {}

for l2 in noun_list:
    dict[l2[0]] = l2[1:]

print(dict)
'''

'''
new_noun_list = str(noun_list)
new_noun_list = new_noun_list.replace(', ', ': ')
print(new_noun_list)
'''

'''
new_noun_list = json.dumps(noun_list)
print(new_noun_list)
'''