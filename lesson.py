# ---------------------------- ex 7 ------------------------------------------
# x = 'a,2,b,5,c,8,a,4,e,11'
# x = x.split(",")
# print(x)
# dict1 = {}
# for i in range(0,len(x),2):
#     key  = x[i]
#     value = int(x[i+1])
#     if key in dict1:
#         dict1[key] += value
#     else:
#         dict1[key] = value
# print(dict1)

# ------------------------------ex 9 --------------------------------------
# list1 =  [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 
# list2 = []
# for i in list1:
#     if i not in list2:
#         list2.append(i)
#     else:
#         continue
# print(list2) 

# point = 0
# dict1 = {
#     "harc1":"a",
#     "harc2":"b",
#     "harc3":"c",
#     "harc4":"d",
#     "harc5":"a",
#     "harc6":"c",
#     "harc7":"d"
# }
# for i in dict1:
#     x = input("mutqagreq patasxan@----")
#     if dict1.get(i) == x:
#         point += 500
#         print(point)
#         if point >= 2500:
#             print("karox eq vercnel dzer gumar@")
#             y = input("yess or no")
#             if y == "yes":
#                 print("duq shahel eq", point,"dram")
#                 break
#             else:
#                 continue

#     else:
#         point = 0 
#         print("duq partveciq", point)
#         break
        
