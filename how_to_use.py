from KahootClass import Kahoot

# 3fd3016c-fd92-440a-a614-5d5c6eb1c17f
# This is the uuid of a random Kahoot I found.
# To see the quizId, look at the host's screen and see the link.
# At the end there will be a part that says 'quizId=(where quizId is)'.
# Put that as the param for the Kahoot class.

# Or you can just do what I did and just prompt asking for the quizID.
kahoot = Kahoot(input("Enter QuizID: "))

for i in range(kahoot.get_quiz_length()):
    if kahoot.get_answer(i) is not None:
        print(f"Question: {kahoot.get_question_names()[i]}\nAnswer: {', '.join(kahoot.get_answer(i))}\n")
