

#  LOOPS

# user_id = "ZeeRox"
# password = "vikas@4ty5"

# user_ids = (
#     'user1',
#     'user2',
#     'user3'
# )

# passwords = (
#     'pass1',
#     'pass2',
#     'pass3'
# )

# credentials = {
#     'user1' : 'password1',
#     'user2' : 'password2',
#     'user3' : 'password3',
#     'user4' : 'password4'
# }

# user_input = input("Enter User Id: ")
# password_input = input("Enter Password: ")

# if user_input not in credentials.keys():
#     print("User not found")

# else:
#     if password_input != credentials[user_input]:
#         print("Wrong password")
#     else:
#         print("Login Successful")


    

# if user_ids == user_input and passwords == password_input:
#     print("Login Successful")
# else:
#     print("Login failed")

# if not(user_ids == user_input):
#     print("Wrong user ID")
# elif not(passwords == password_input):
#     print("Worng password")
# else:
#     print("Login Successful")


# sentiment analysis

# user_feedback = "The song is fantastic and one of the best in my playlist"
# neg_feedback_words = (
#     'bad','worst','trash','stupid'
# )
# pos_feedback_words = (
#     'good','best','awesome','fantastic'
# )


# neg_count: int = 0
# pos_count: int = 0
# for word in user_feedback.split(' '):
#     if word in neg_feedback_words:
#         neg_count += 1
#     if word in pos_feedback_words:
#         pos_count += 1
# if neg_count > pos_count:
#     print("bad review")
# else:
#     print("good review")


# list comprehension: we are making 

""" [<action> for <element to be acted on> in <list>]"""
"""
for word in words:
    word = word.lower()
    words.append(word)
"""

from ForFunctionOnly import *
User_feedback1 = "The 'Remember me' song is fantastic, one of the favorite song in my playlist."
User_feedback2 = "The 'Remember me' song is bad, one of te worst song in my playlist."
feedbacks = [User_feedback1,User_feedback2]
output = list(map(sentiment_analysis, map(clean_data,feedbacks)))
print("Good reviews overall ") if output.count(True) > output.count(False) else print("No reviews overall")


# print("Song is Good") if sentiment_analysis(clean_data(feedback)) else print("Song is Bad")
# do x if y is true else do z