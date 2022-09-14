#Create a program that prompts the user for 3 bowling scores. The program should then display the 3 scores and the average
#the program should then display the 3 scores and the average.
amount_of_scores = 3

#program intro
print('*********************************')
print('**Welcome to my Bowling Program**')
print('*********************************')

#do inputting here and converting scores to integers
print("Enter your 3 scores")
score_1 = int(input('Enter your first bowling score: '))
score_2 = int(input('Enter your second bowling score: '))
score_3 = int(input('Enter your third bowling score: '))

#do processing here
average = (score_1 + score_2 + score_3) / amount_of_scores

#do outputting here
print('Your scores are' , score_1 , score_2 , score_3 , 'Your Average score is: {:.2f}' .format(round(average)))
print("Thank you! You are a great bowler")