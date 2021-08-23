import time 
from pygame import mixer as audio

def rules():
    print('-------->Welcome to the Healthy Programmer<-------- ')
    print('What this program do--> When you are in office then Run this programme .\n1.) It will remind you that you have to drink 3.6 liters of water in your office time .\n2.) It will remind you that you have to do your exercise in every 30 minutes .\n3.) It will remind you that you have to do some Physical Exercise in every 45 minutes .')

def func(e):
    f=open(f'{e}.txt','a')
    f.write('['+time.asctime(time.localtime(time.time()))+']\n')
    audio.init()
    audio.music.load(f"./exercise-7/{e}.mp3")
    audio.music.play()
    while True:
        print("Type 'done' to stop playing this song")
        query = input()
        if query == 'done':
            audio.music.stop()
            break
        else:
            continue
        break

    #                Main Program Start from here      
rules()
while(True):
    start=input('Do you wanted to start this Programme? Yes or No\n')
    if start=='yes':
        while(True):
            print('Thank you Sir ! For using this programme This will make sure to improve your health')    
            what=input("->")
            if what=='water':
                func(what)
            elif what=='eyes':
                func(what)
            elif what=='exercise':
                func(what)
            break
    elif start=='no':
        print("Thank you for reading about this programme. Hope you will use me in the Future")
        break
    else:
        print('Type yes or no only ')

# #Healthy Programmer
# # 9am - 5pm
# # Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# # Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# # Physical activity - physical.mp3 every - 45 min - ExDone - log
# # Rules
# # Pygame module to play audio

# from pygame import mixer
# from datetime import datetime
# from time import time

# def musiconloop(file, stopper):
#     mixer.init()
#     mixer.music.load(file)
#     mixer.music.play()
#     while True:
#         input_of_user = input()
#         if input_of_user == stopper:
#             mixer.music.stop()
#             break

# def log_now(msg):
#     with open("mylogs.txt", "a") as f:
#         f.write(f"{msg} {datetime.now()}\n")

# if __name__ == '__main__':
#     # musiconloop("water.mp3", "stop")
#     init_water = time()
#     init_eyes = time()
#     init_exercise = time()
#     watersecs = 2
#     exsecs = 2
#     eyessecs = 2

#     while True:
#         if time() - init_water > watersecs:
#             print("Water Drinking time. Enter 'drank' to stop the alarm.")
#             musiconloop('water.mp3', 'drank')
#             init_water = time()
#             log_now("Drank Water at")

#         if time() - init_eyes >eyessecs:
#             print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
#             musiconloop('eyes.mp3', 'doneeyes')
#             init_eyes = time()
#             log_now("Eyes Relaxed at")

#         if time() - init_exercise > exsecs:
#             print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
#             musiconloop('exercise.mp3', 'donephy')
#             init_exercise = time()
#             log_now("Physical Activity done at")

