def gradingStudents(grades):
    round = []
    for grade in grades:
        if grade > 40:
            next_mul_of_five= (grade // 5 +1)*5
            if  next_mul_of_five<3:
                print("DASda")
                round.append(next_mul_of_five)
            else:
                round.append(grade)
        else:
            round.append(grade)    
            
    return round
    
print(gradingStudents([73
,67
,38,
33]))
