lost_items = []

def add_item(id, name, desc, location,date,status):
    item = {}
    item["id"] = id
    item["name"] = name
    item["description"] = desc
    item["location"] = location
    item["date"] = date
    item["status"] = status
    lost_items.append(item)
    return f"Item added successfully!!"

def name(item,name):
    item["name"] = name
    return f"Changed successfully!!"
    
def desc(item,desc):
    item["description"] = desc
    return f"Changed successfully!!"

def location(item,location):
    item["location"] = location
    return f"Changed successfully!!"

def date(item,date):
    item["date"] = date
    return f"Changed successfully!!"

def claimed(item):
    item["status"] = "Claimed"
    return f"Changed successfully!!"

def unclaimed(item):
    item["status"] = "UnClaimed"
    return f"Changed successfully!!"

def view_items():
    if lost_items:
        return lost_items
    else:
        return f"Error"
             

def search_items(search_item):
    lost = []
    for item in lost_items:
        keyword = ""
        keyword += item["name"]
        keyword += item["description"]
        keyword = keyword.strip().lower()
        if search_item in keyword:
            lost.append(item)
    return lost
def update_items(id):
    for item in lost_items:
        if item["id"] == id:
            return item

def delete_item(delete_item):
    for item in lost_items:
        if item["id"] == delete_item:
            lost_items.remove(item)
            return f"Item deleted successfully!!"
            