import item

unique_id = 1
while True:
    print(f"**********LOST AND FOUND SYSTEM**********")
    print(f"1. Report a found item\n"
      f"2. View all found items\n"
      f"3. Search for an item\n"
      f"4. Update an item\n"
      f"5. Delete an item\n"
      f"6. Exit the application"      
      )
    try:
        action = int(input("Enter an option from the menu(1-6): "))
        if action <= 0 or action > 6:
            print("Enter a valid option from menu(1-6)!!")
            continue
    except ValueError:
        print("Enter a valid option from menu(1-6)!!")
        continue
    
    
    if action == 1:
        id = unique_id
        name = input("Enter the item's name: ")
        description = input("Enter the item's description: ")
        location = input("Where was it found? ")
        date = input("Which date was it found,(m/d/y): ")
        status = "UnClaimed"
        unique_id += 1
        print(item.add_item(id=id,name=name,desc=description,location=location,date=date,status=status))
  
    elif action == 2:
        print(">>>LOGGED ITEMS<<<")
        all_items = item.view_items()
        if all_items == "Error":
            print("Sorry, no items have been logged yet!!")
        else:  
            for object in all_items:
                for key, value in object.items():
                    print(key,": ",value)
                    
    elif action == 3:
        search_item = input("Enter the item's name or it's description: ")
        search_item = search_item.strip().lower()
        if search_item == "":
            print("Enter something to search!!")
            continue
        found = item.search_items(search_item)
        if found == []:
            print("Keyword is incorrect or item hasn't been logged yet, view all items and/or try again.")
        else:
            print("=====ITEM DETAILS====")
            for record in found:
                for key, value in record.items():   
                    print(key,": ",value) 
                print("=========================")    

    elif action == 4:
        try:
            id = int(input("Enter the item's id to be updated: "))
        except ValueError:
            print("Invalid id!!")
            continue
        found = item.update_items(id)
        if found == None:
            print("Keyword is incorrect or item hasn't been logged yet, view all items and/or try again.") 
            continue                  
        else:
            print("=====ITEM DETAILS====")
            for key, value in found.items():   
                print(key,": ",value) 
        try:  
            detail = int(input(f"Which field do you  want to modify?(choose corresponding number 1,2,3,4 or 5) \n"
                               f"1. name\n"
                               f"2. description\n"
                               f"3. location\n"
                               f"4. date\n"
                               f"5. status\n"
                               f"Enter field here: "
                               ) )   
        except ValueError:
            print("Enter a valid field number(1-5)")
            continue
        if detail == 1:
            new_name = input("Enter its new name: ")
            print(item.name(found,new_name))
        elif detail == 2:
            new_desc = input("Enter its new description: ")
            print(item.desc(found,new_desc))
        elif detail == 3:
            new_location = input("Where was it found: ") 
            print(item.location(found,new_location))
        elif detail == 4:
            new_date = input("Enter the new date: ")  
            print(item.date(found,new_date))
        elif detail == 5:
            try:
                new_status = int(input("Enter 0 if unclaimed and 1 if claimed: "))
            except ValueError:
                print("Invalid status!!, choose 0 or 1")
                continue
            if new_status != 0 and new_status != 1:
                print("Invalid status!!, choose 0 or 1")
            elif new_status == 0:
                print(item.unclaimed(found))
            elif new_status == 1:
                print(item.claimed(found))
        else:
            print("Enter a valid field number(1-5)")
            
                
                
    elif action == 5:
        try:
            delete_item = int(input("Enter the id of the item you want to delete: "))
            message = item.delete_item(delete_item)
            if message == None:
                print("Item doesn't exist/incorrect id!!")
            else:
                print(message)
        except ValueError:
            print("Enter a valid id!!")

    elif action == 6:
        print("Bye Bye!!")
        break        
                