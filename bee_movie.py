from fbchat import Client
from fbchat.models import *
import time

bee = open('bee_movie_script.txt')
lines = bee.readlines()

client = Client('<email>', '<password>')

#or <group id> and ThreadType.GROUP for groups
for line in lines:
    client.send(Message(text=line), thread_id='<user id>', thread_type=ThreadType.USER) 
    time.sleep(1)


client.logout()