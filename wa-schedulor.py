import pywhatkit  # python moudule for whatsapp message schedulur

class color:   # for printing
    UNDERLINE = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'

# welcome loop()
def welcome():
    print(color.UNDERLINE + "Choose '1' or '2' from below:" + color.END)
    print(color.BOLD + "1. Send to a Number" + color.END)
    print(color.BOLD + "2. Send to a Group" + color.END)
    send = int(input("Choose: "))
    if send == 1:
        send_to_number()
    elif send == 2:
        send_to_group()

# send to group loop()
def send_to_group():
    msg = str(input("your message: "))
    groupidinfo = "Group ID is something that is in its invite line \n https://chat.whatsapp.com/AB123CDEFGHijklmn, here AB123CDEFGHijklmn is group ID"
    print(groupidinfo)
    group_id = str(input("group id: "))
    print(color.BOLD + "12-hour format" + color.END)
    time_hour = int(input("hour: "))
    time_minute = int(input("minute: "))
    print(color.BOLD + "1 for AM" + color.END, "or", color.BOLD + "2 for PM" + color.END)
    am_pm = int(input("Choose: "))
    if am_pm == 2:
        time_hour+=12
    pywhatkit.sendwhatmsg_to_group(group_id, msg, time_hour, time_minute)
    welcome()

# Send to number loop
def send_to_number():
    msg = str(input("your message: "))
    print(color.UNDERLINE + "Phone number with Country Code" + color.END)
    number1 = str(input("Country Code:"))
    number2 = str(input("Phone number:"))
    number = str(number1 + number2)
    print(number)
    print(color.BOLD + "12-hour format" + color.END)
    time_hour = int(input("hour: "))
    time_minute = int(input("minute: "))
    print(color.BOLD + "1 for AM" + color.END, "or", color.BOLD + "2 for PM" + color.END)
    am_pm = int(input("Choose: "))
    if am_pm == 2:
        time_hour+=12
    pywhatkit.sendwhatmsg(number, msg, time_hour, time_minute)
    welcome()

welcome()