#if statement = helps decision making

age = int(input('How old are you?:'))

if age >= 18: #remember the colon!
    print('Come on in!') #indent will tell you you're working in your if statement
elif age >= 65: #remember these are sequential. A number higher than 65 won't give the senior discount because we already hit the 'come on in' step.
    print('Senior discount!')
elif age <=4:
    print('How did you get here alone?')
else: #COLON!
    print('Sorry bud... not old enough')
