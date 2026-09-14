age = 16
has_permit = True

if age >= 16 and has_permit:
    print("You can take the driving test.")
else:
    print("You cannot take the driving test.")

player_level = 50
has_vip_pass = False

if player_level >= 50 or has_vip_pass:
    print("VIP access granted")
else: print("VIP access denied")

is_banned = True
if not is_banned:
    print("You can join the server")
else:
    print("You are banned from the server")


player_level = 35
is_banned = False

if player_level >= 35 and not is_banned:
    print("You can enter the tournament")
else:
    print('You cannot enter the tournament')