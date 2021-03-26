def find_average(query_name, dictt): #find average of list in a dictionary 
    ans = 0
    if( query_name in dictt):
        ans = sum(dictt[query_name])/len(dictt[query_name])
    # return round(ans, 2)
    print("{:.2f}".format(ans))


if __name__=="__main__":

    student_marks = {}
    for _ in range(int(input())):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    # print(student_marks)
    query_name = input()
    find_average(query_name, student_marks)
