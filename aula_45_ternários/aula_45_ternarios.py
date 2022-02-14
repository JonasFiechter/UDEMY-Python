# Ternarios...

logged_user = True

msg = f'User on {logged_user}' if logged_user else f'User must log in!'
print(msg)

age = 19
msg = f'User can log in' if age > 18 else f'User cannot log in'
print(msg)