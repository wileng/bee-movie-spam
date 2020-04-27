from fbchat import Client
from fbchat.models import *
import time

#opens the movie script and creates a list, with each line being an item
bee = open('bee_movie_script.txt')
lines = bee.readlines()

#login to your FB account
client = Client('<email>', '<password>')

#use these to search for user/group IDs
client.searchForUsers('<person name here>')
client.searchForGroups('group name here')

#loop that goes through the script/list and sends messages
for line in lines:
    #Could use <group id> and ThreadType.GROUP for groups
    client.send(Message(text=line), thread_id='<user id>', thread_type=ThreadType.USER) 
    #1 second delay
    time.sleep(1)

#logout of account
client.logout()