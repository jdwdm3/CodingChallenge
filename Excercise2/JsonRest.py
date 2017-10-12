################################################################inp##########
##                                                                      ##
##          Jeremy Warden -- Gateway Blend Coding Challenge             ##
##                                                                      ##
##########################################################################

####### Import Section #######
import requests
import json
##############################

def main():

    #Perform a get request
    response = requests.get('http://jsonplaceholder.typicode.com/todos')

    #Iterate through the json items
    #for item in response.json():
        #print(item)

    #Expect status code 200 on success
    print(response.status_code)

    #Create a Todo
    My_user = {'userId': 27, 'id': 2727, 'title': 'This is my User', 'completed': True}
    json_data = json.dumps(My_user)
    response = requests.post('http://jsonplaceholder.typicode.com/todos', data = json_data)

    #Expect status code 201 on success
    print(response.status_code)

    '''
    Delete had me stumped a bit, I am assuming it will find the object that I send it and remove it,
    I would love to discuss this with you guys and get an explanation on how exactly delete works
    The status code is 404, which is not good.  I was assuming to start it would not let me do anything excet get the data
    when I first began, but it appears the status code was acceptbale for a post request. 
    '''
    response = requests.delete('http://jsonplaceholder.typicode.com/todos', data = json_data)
    print(response.status_code)
    
    
#########
main()
