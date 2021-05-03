import time,random,os,datetime,itertools
from pyfiglet import Figlet

whyaretheresomanyvariables = 0

def render(text,style):
    f = Figlet(font=style)
    print(f.renderText(text))


while True:
    os.system("clear")
    render("a timer program",'slant')
    print("Please select a menu position.\n")
    print("1. Show your system time using pyfiglet.\n2. Timer\n3. Take a break!\n4. To-do list\n5. Quit")
    question = input("Select a number (1/2/3): ")

    if question == "1":
        for __ in itertools.repeat(1):
            # update time every second, clear the screen and display the time using pyfiglet
            e = datetime.datetime.now()
            os.system("clear")
            render(f'{e.strftime("%Y-%m-%d %H:%M:%S")}','slant')
            print("updated!")
            time.sleep(1)
    if question == "2":
        timer = input("How many minutes you want to set timer on?: ")
        why = float(timer)
        lastone = why * 60
        print(lastone)
        for __ in itertools.repeat(1):
            os.system("clear")
            render("Timer",'slant')
            print(f'Minutes left: {why}\nSeconds left: {lastone}')
            time.sleep(1)
            whyaretheresomanyvariables += 1
            lastone -= 1
            if lastone == 0:
                os.system('notify-send -i ~/timerandsleep/Magis_Tempo-Wanduhr_800x800-ID44985-4efdfc13c9fc7cee4710da43ef30b854.jpg "Time is up!" "Timer ran up!"')
                os.system('mpg123 ~/timerandsleep/iPhone\ Radar\ AlarmRingtone\ \(Apple\ Sound\)\ -\ Sound\ Effect\ for\ Editing.mp3 ')
                break
            if whyaretheresomanyvariables == 60:
                why -= 1
                whyaretheresomanyvariables = 0

    if question == "3":
        timer = input("you want to receive a message every x minutes (change x to your input, for example, 30 - a mesage every 30 minutes): ")
        waitforme = float(timer)
        whyiammakingsomanyvariables = waitforme * 60
        for __ in itertools.repeat(1):
            time.sleep(whyiammakingsomanyvariables)
            os.system('notify-send -i ~/timerandsleep/Magis_Tempo-Wanduhr_800x800-ID44985-4efdfc13c9fc7cee4710da43ef30b854.jpg "Take a break!" "To keep your eyes healthy, please take a 5 minute break from your computer!"')
    
    if question == "4":
        todo = []
        for __ in itertools.repeat(1):
            os.system("clear")
            addtodo = input("What do you want to add to your list?: ")
            todo.append(addtodo)
            print('\nTo do list:')
            print('\n- '.join(map(str, todo)))
            time.sleep(5)

    if question == "5":
        quit()