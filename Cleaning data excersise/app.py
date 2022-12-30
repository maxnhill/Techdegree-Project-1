from data import data


# INSTRUCTIONS
# 1) Split the full name into two fields, first name and last name

def clean_data(data):
    data_2= []
    for user in data:
        fixed={}
        fixed['email']= user['email']
        first_last= user['name'].split(" ")
        fixed['First_name']= first_last[0]
        fixed['Last_name']=first_last[1]
    # 2) Convert the admin field to a boolean value
        if user['admin']== "True":
            user['admin'] = True
        else:
            user['admin']= False
            
    # 3) Convert the id to an integer
        fixed['id']= int(user['id'])
        data_2.append(fixed)
                            
    return data_2
    
                            
print(clean_data(data))                           
# 5) Complete this in a function(s)
# 6) Save the data into a new data structure: a list of dictionaries
   