# zip(*iterables) = aggregate elements from 2 or more iterables (list, tuples, etc.)
# creates a zip object with paired elements stored in tuples for each element

usernames = ['Dude', 'Bro', 'Mister']
passwords = ['1234qwer', 'password', 'admin']

users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key + ' ' + value)

login_date = ['1/1/11', '2/2/22', '3/3/93']

defined_users = list(zip(usernames,passwords,login_date))

for i in defined_users:
    print(i)


