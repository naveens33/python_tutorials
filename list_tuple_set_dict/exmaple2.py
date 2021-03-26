"""Students of District College have a subscription to English and French newspapers. Some students have subscribed
to only the English newspaper, some have subscribed to only the French newspaper, and some have subscribed to both
newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has
subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only
English newspapers. """

eng_total=int(input())
eng_roll_no=set(input().split(' '))
fre_total = int(input())
fre_roll_no = set(input().split(' '))
total_stu = eng_total+fre_total
if total_stu > 0 and total_stu < 100:
    eng_roll_no.difference_update(fre_roll_no)
    print(len(eng_roll_no))