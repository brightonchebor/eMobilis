print('Enter your score out of 100:')
user_score = int(input('> '))

if user_score >= 90 and user_score <= 100:
    print('Your grade is: A')
elif user_score >= 80 and user_score < 90:
    print('Your grade is: B')
elif user_score >= 70 and user_score  < 80:
    print('Your garde is: C')
elif user_score >= 60 and user_score < 70:
    print('Your grade is: D')
elif user_score < 60 and user_score > 0:
    print('Your grade is: F')
else:
    print('Please enter your score out of 100')
