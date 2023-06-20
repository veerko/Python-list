

#PYTHON LIST

camping_list = ["knife", "tent", "food", "water", "sleeping bags", "coffee"]

camp_site = ["Lake", 404, 28.3, True]

#instead of adding it to the list we use "append" 
camping_list.append("phone")
camping_list.append("charger")
camping_list.append("flash drive")
camping_list.append("ethernet")
camping_list.append("rasperry pi")
#instead of append we can also use extend, where on append we can only add 1 item in a row, but with extend we can add more in the same row
camping_list.extend(["tobak, snus"])

#how to remove something with pythons in built classes
camping_list.remove ("tent")

camping_list.pop (4)
print (camping_list)


