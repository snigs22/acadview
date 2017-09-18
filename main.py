from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

print "Hello! Let\'s get started"

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = raw_input(question)


def start_chat(spy_name, spy_age, spy_rating, spy_salutation):
    current_status_message = None

    spy_name = spy_salutation + " " + spy_name

    if spy_age > 12 and spy_age < 50:
        print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"
        show_menu = True
        while show_menu:
            print "1.status of spy"
            print "2.status update"
            print "3.add a spy"
            print "4.send a message"
            print "5.read a message"

    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing == "Y":
    start_chat(spy_name, spy_age, spy_rating,spy_salutation)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy_name) > 0:
        spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy_age = input("What is your age?")

        spy_rating = raw_input("What is your spy rating?")

        spy_is_online = True

        start_chat(spy_name, spy_age, spy_rating,spy_salutation)
    else:
        print 'Please add a valid spy name'