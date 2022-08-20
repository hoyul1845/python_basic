absent = [2, 5] # 결석
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue
    print("{0}, 책을 읽어봐".format(student))