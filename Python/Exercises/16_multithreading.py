# multithreading : utilizing multiple threads to facilitate multitasking
from threading import Thread
import time

def walk_dog(dog_name):
    time.sleep(8)
    print(f"You walk {dog_name}.")
    
def take_trash():
    time.sleep(2)
    print("You take out the trash.")
    
def check_mail():
    time.sleep(6)
    print("You check the mail.")

# walk_dog()
# take_trash()
# check_mail()
    
chore1 = Thread(target=walk_dog, args=("Damon",)) # for passing arguments create a tuple () followed by a comma,
chore1.start()

chore2 = Thread(target=take_trash)
chore2.start()

chore3 = Thread(target=check_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("All chores complete.")
    