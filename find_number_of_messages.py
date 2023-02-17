from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    sum=0
    for i in data['messages']:
        if i['type']=='message':

            sum+=1
    return sum

path='data/result.json'

print(find_number_of_messages(read_data(path)))