import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# What percentage on next Lab Exam is needed for 86 average percentage in overall grade

fake_exam_score = float(input('\n \n Please input a score for your next exam (format 0.00): '))
#use scores series data for exams (263) to add a number out of 100
#take this new total for exams and weight it (* .5)
#store it in a variable for new percent for percents at index 0

predicted_exam_scores_total = 263.00+fake_exam_score
predicted_exam_percents_avg = ((fake_exam_score / 100.00)+(0.8766))/2

grade_types = pd.Series(['Lecture Exams', 'Lab Exams', 'Homework'])

#hardcode changing 0.8267 to 0.8766
percents = pd.Series([predicted_exam_percents_avg, 0.6533, 0.9413])
89
weight_percents = pd.Series([0.50, 0.20, 0.30])

#hardcode changing 248 to 263 for the extra credit
scores = pd.Series([predicted_exam_scores_total, 261.33, 1317.84])

#change 300 to 400
full_scores = pd.Series([400.00, 400.00, 1400.00])

#in score points
#extra_credit = 15

df = pd.DataFrame({'group': grade_types,
                    'percentage': percents,
                    'weight': weight_percents,
                    'score_out_of': scores,
                    'full_score': full_scores
                    })

type(df)
print(df)

weighted_grades = (percents * weight_percents)
#print(weighted_grades)
#weighted_grade = (weighted_grades.sum()) - (248.00 * 0.50) + (263.00 * 0.50)
weighted_grade = (weighted_grades.sum())
type(weighted_grade)
print('Weighted overall grade is: ')
print(weighted_grade * 100)
#print(263.00 / 3)

#input 87.66 to check current grade before next exam