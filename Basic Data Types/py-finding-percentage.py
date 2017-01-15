from __future__ import division
n = int(raw_input())
student_marks = {}
for _ in range(n):
    line = raw_input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = raw_input()
score_list = []
total = 0
if query_name in student_marks:
    score_list = student_marks.get(query_name)
    for i in range(len(score_list)):
        total += score_list[i]
avg = total / 3
print "{0:.2f}".format(avg)
