case_count = int(input())
# case_count = 1
student_list = []
result_list = []

while case_count:
    student_list = [int(x) for x in input().split(' ')]
    # student_list = [5, 50, 50, 70, 80, 100]
    # student_list = [7, 100, 95, 90, 80, 70, 60, 50]
    # student_list = [3, 70, 90, 80]
    # student_list = [9, 100, 99, 98, 97, 96, 95, 94, 93, 91]
    # student_list = [5, 50, 50, 70, 80, 100]

    if 1 > student_list[0] or student_list[0] > 1000:
        print("정상적이지 않은 학생의 수 입니다.")
        break
    elif student_list[0] != len(student_list[1:]):
        print("갯수가 일치하지 않습니다.")
        break

    student_list = student_list[1:]
    ratio = sum(student_list) / len(student_list)
    ratio_count = 0
    for x in student_list:
        if 0 > x or 100 < x:
            print("정상적이지 않은 점수 값 입니다.")
            exit()
        if ratio < x:
            ratio_count += 1

    result_string = f"{ratio_count / len(student_list) * 100:.3f}%"
    result_list.append(result_string)

    case_count -= 1

for x in result_list:
    print(x)

