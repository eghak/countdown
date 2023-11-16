import datetime

user_input = input("Enter your goal with a deadline separated by colon: ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# convert the deadline string data type to a datetime data type
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

# today's date
today_date = datetime.datetime.today()

# calculate how many days from now until deadline
days_to_deadline = deadline_date - today_date

print("You have", days_to_deadline, "until the deadline to", goal)

# if we just want to see the days left without the time
print("You have", days_to_deadline.days, "days until the deadline to", goal)
