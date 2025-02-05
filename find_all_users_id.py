from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    id = []
    for user in data["messages"]:
        if user.get("actor_id") != None:
            
                id.append(user["actor_id"])
        elif user.get("from_id"):
            
                id.append(user["from_id"])
        p=set(id)
        
    print(list(p))

data = read_data("data/result.json")
print(find_all_users_id(data))