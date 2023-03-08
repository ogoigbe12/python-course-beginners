command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            started = True
            print('car started')
    elif command == "stop":
        if not started:
            print("car stopped already!")
        else:
            started = False
            print("stopped car")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command == "quit":
        break
    else:
        print("I don't understand that")