# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

#score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
#print(score_file.readline(), end="")
#print(score_file.readline(), end="")
#print(score_file.readline(), end="")
#score_file.close

#score_file = open("score.txt", "r", encoding="utf8")
#while True:
    #line = score_file.readline()
   # if not line:
  #      break
 #   print(line, end="")
#score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
    
score_file.close()