correct_answers = ["H", "U", "Z", "A", "I","F","A"]
user_answers = []
attempted = 0
while True:
    answer = input("Enter your answer atleast 7 times: ")
    if answer == "quit":
        break
    else:
        user_answers.append(answer)
        attempted +=1
def grade_quiz(user_answers, correct_answers):
    score = 0
    for i in range(5):
        if user_answers[i] == correct_answers[i]:
            score += 1
    percentage = (score / len(correct_answers)) * 100
    return {"score": score, "attempted": attempted, "percentage": percentage}

print(grade_quiz(user_answers, correct_answers))
