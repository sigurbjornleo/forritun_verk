temp_now = int(input("Current temperature (C°): "))
temp_prev = int(input("Previous temperature (C°): "))
action_str = ""
RAISE = "raise"
KEEP = "keep"
LOWER = "lower"
SHUTDOWN = "shutdown"
if temp_now >= 350:
    action_str = SHUTDOWN
elif temp_now < 300 and temp_now == temp_prev:
    action_str = RAISE
elif temp_now < 300 and temp_now > temp_prev:
    action_str = KEEP
elif temp_now == 300:
    action_str = KEEP
elif temp_now > 300 and temp_now >= temp_prev:
    action_str = LOWER
elif temp_now > 300 and temp_now < temp_prev:
    action_str = KEEP


print(action_str)

# ... implement control logic and print the appropriate action