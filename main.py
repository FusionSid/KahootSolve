# Simple kahoot cheat

import requests
import os

url = input("Enter the kahoot id/link: ")

kahoot_id = url.split('quizId=')[-1]
print(kahoot_id)

answers_url = 'https://create.kahoot.it/rest/kahoots/{kahoot_id}/card/?includeKahoot=true'.format(kahoot_id=kahoot_id)
data = requests.get(answers_url).json()

os.system("clear")

for q in data['kahoot']['questions']:
    for choice in q['choices']:
        if choice['correct']:
            break
    question = q['question'].replace('&nbsp;', ' ')
    answer = choice['answer'].replace('&nbsp;', ' ')
    for i in ["<b>", "<i>", "</b>", "</i>"]:
        question = question.replace(i, "")
        answer = answer.replace(i, "")
    print('Q: {:<70}\n\nA: {} '.format(question, answer))
    input()
    os.system("clear")
    