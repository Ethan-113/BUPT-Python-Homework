if __name__ == '__main__':
    count = 0
    total = 0
    num_student = int(input())
    grades = input()
    num_grades = [int (x) for x in grades.split()]

    for i in range(len(num_grades)):
        if num_grades[i] >= 60:
            count += 1

        total += num_grades[i]

    average = round(total/len(num_grades), 1)

    print("average = " + str(average))
    print("count = " + str(count), end="")