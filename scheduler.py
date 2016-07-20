#! python3
# this is a scheduler that will have three components:
#       * Take in your task
#       * Ask you for when you'd like it done by
#       * Say hi to you when you initiate program
#       * Ask you if there is anything else you'd like?
#       * Exit if there isn't (No, or space)

#print("Hi! I am a scheduler. I am here to help you with your needs. :) ")
#print('Say hi!')
def taskTaker():
    if input() == 'hi!':
        tasks = []
        tasks.append(input("What would you like to do today? "))
        tasks[0].split()
        print(tasks)
    print()
taskTaker()
