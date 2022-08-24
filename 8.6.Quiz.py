for i in range(1, 51):
    with open(str(i) + "주자.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주가보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")