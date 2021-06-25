import csv


class Student:
    def __init__(self, student_id, first_name, last_name):
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def add_student(self, student):
        with open('Student.csv', 'a') as file:
            file.write("%s,%s,%s\n" % (student.student_id, student.first_name, student.last_name))

    def read_student(self, student_id):
        student_details = {}

        with open('Student.csv', newline="") as file:
            for line in file.readlines():
                line_list = line.split(',')
                if line_list[0] == student_id:
                    student_details[student_id] = [line_list[1], line_list[2]]
            if not student_details:
                print("Enter a valid student id.")
        return student_details

    def __str__(self):
        return "%s,%s,%s" % (self.student_id, self.first_name, self.last_name)


class Policy:
    def __init__(self):
        self.__a_num = None
        self.__t_num = None
        self.__f_num = None
        self.__a_wt = None
        self.__t_wt = None
        self.__f_wt = None
        self.__policy = {}

    @property
    def a_num(self):
        return self.__a_num

    @a_num.setter
    def a_num(self, a_num):
        self.__a_num = a_num

    @property
    def t_num(self):
        return self.__t_num

    @t_num.setter
    def t_num(self, t_num):
        self.__t_num = t_num

    @property
    def f_num(self):
        return self.__f_num

    @f_num.setter
    def f_num(self, f_num):
        self.__f_num = f_num

    @property
    def a_wt(self):
        return self.__a_wt

    @a_wt.setter
    def a_wt(self, a_wt):
        self.__a_wt = a_wt

    @property
    def t_wt(self):
        return self.__t_wt

    @t_wt.setter
    def t_wt(self, t_wt):
        self.__t_wt = t_wt

    @property
    def f_wt(self):
        return self.__f_wt

    @f_wt.setter
    def f_wt(self, f_wt):
        self.__f_wt = f_wt

    @property
    def policy(self):
        return self.__policy

    @policy.setter
    def policy(self, policy):
        self.__policy = policy

    def set_semester(self):

        no_of_assignments = int(input("Enter number of programming assignments(0-6)"))
        while no_of_assignments < 0 or no_of_assignments > 6:
            print("Enter valid range (0-6)")
            no_of_assignments = int(input("Enter number of programming assignments(0-6)"))
        self.a_num = no_of_assignments
        self.policy['Assignment Num'] = no_of_assignments

        no_of_tests = int(input("Enter number of tests(0-4): "))
        while no_of_tests < 0 or no_of_tests > 4:
            print("Enter valid range (0-4): ")
            no_of_tests = int(input("Enter number of tests(0-4): "))
        self.t_num = no_of_tests
        self.policy['Test Num'] = no_of_tests

        no_of_final_exam = int(input("Enter number of Final exams (0-1): "))
        while no_of_final_exam < 0 or no_of_final_exam > 1:
            print("Enter valid range (0-1)")
            no_of_final_exam = int(input("Enter number of Final exams (0-1): "))
        self.f_num = no_of_final_exam
        self.policy['Final Exam Num'] = no_of_final_exam

        print("Enter the weights for Assignment, Test and Final exam: ")
        print("Weights must add to 100%")

        assignment_wt = float(input("Please enter the weight percentage of programming assignments: "))
        self.a_wt = assignment_wt
        self.policy['Assignment Weight'] = assignment_wt

        test_wt = float(input("Please enter the weight percentage of tests: "))
        self.t_wt = test_wt
        self.policy['Test Weight'] = test_wt

        final_exam_wt = float(input("Please enter the weight percentage of final exams: "))
        self.f_wt = final_exam_wt
        self.policy['Final Exam Weight: '] = final_exam_wt

    def write_policy(self):
        with open('Policy.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Assignments Number', self.__a_num])
            writer.writerow(['Tests Number', self.__t_num])
            writer.writerow(['Final Exam Number', self.__f_num])

            writer.writerow(['Assignment Weight', self.__a_wt])
            writer.writerow(['Test Weight', self.__t_wt])
            writer.writerow(['Final Exam Weight', self.__f_wt])

    def read_policy(self):
        policy = {}
        with open('Policy.csv', newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                policy[row[0]] = row[1]

        return policy


class Score:
    def __init__(self):
        self.__student_id = None
        self.__type_of_score = None
        self.__number = None
        self.__change_score = None
        self.__assignment_score = None

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def type_of_score(self):
        return self.__type_of_score

    @type_of_score.setter
    def type_of_score(self, type_of_score):
        self.__type_of_score = type_of_score

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def change_score(self):
        return self.__change_score

    @change_score.setter
    def change_score(self, change_score):
        self.__change_score = change_score

    @property
    def assignment_score(self):
        return self.__assignment_score

    @assignment_score.setter
    def assignment_score(self, assignment_score):
        self.__assignment_score = assignment_score

    @property
    def test_score(self):
        return self.__test_score

    @test_score.setter
    def test_score(self, test_score):
        self.__test_score = test_score

    @property
    def final_score(self):
        return self.__final_score

    @final_score.setter
    def final_score(self, final_score):
        self.__final_score = final_score

    def write_score(self, student_id, exam_type, number, score):
        with open('Scores.csv', 'a') as file:
            file.write("%s,%s,%s,%s\n" % (student_id, exam_type, number, score))

    def record_score(self, change_score, number, student_id, type_of_score):
        if type_of_score == "A":
            type_of_score = "Assignment"
            self.update_score(change_score, number, student_id, type_of_score)
        elif type_of_score == "T":
            type_of_score = "Test"
            self.update_score(change_score, number, student_id, type_of_score)
        elif type_of_score == "F":
            type_of_score = "FinalExam"
            self.update_score(change_score, number, student_id, type_of_score)
        else:
            print("Unsupported type of score, please enter the correct one.")

    def update_score(self, change_score, number, student_id, type_of_score):
        lines = list()
        with open('Scores.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for i in range(len(lines)):
                    if lines[i][0] == student_id and lines[i][1] == type_of_score and lines[i][2] == number:
                        lines.remove(lines[i])
                        update_line = [student_id, type_of_score, number, change_score]
                        lines.append(update_line)
        with open('Scores.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

    def calculate_final_score(self):
        policy = Policy()
        lines = list()
        dict_student_id_score = {}

        with open('Scores.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)

        for i in range(len(lines)):

            if lines[i][0] in dict_student_id_score.keys() and lines[i][1] == "Assignment":
                if "Assignment" in dict_student_id_score[lines[i][0]]:
                    assignment_score = float(dict_student_id_score[lines[i][0]]['Assignment'])
                    assignment_score += float(lines[i][3])
                    dict_student_id_score[lines[i][0]]['Assignment'] = assignment_score
                else:
                    dict_student_id_score[lines[i][0]][lines[i][1]] = float(lines[i][3])
            elif lines[i][0] in dict_student_id_score.keys() and lines[i][1] == "Test":
                if "Test" in dict_student_id_score[lines[i][0]]:
                    test_score = float(dict_student_id_score[lines[i][0]]['Test'])
                    test_score += float(lines[i][3])
                    dict_student_id_score[lines[i][0]]['Test'] = test_score
                else:
                    dict_student_id_score[lines[i][0]][lines[i][1]] = float(lines[i][3])
            elif lines[i][0] in dict_student_id_score.keys() and lines[i][1] == "FinalExam":
                if "FinalExam" in dict_student_id_score[lines[i][0]]:
                    final_exam_score = float(dict_student_id_score[lines[i][0]]['FinalExam'])
                    final_exam_score += float(lines[i][3])
                    dict_student_id_score[lines[i][0]]['FinalExam'] = final_exam_score
                else:
                    dict_student_id_score[lines[i][0]][lines[i][1]] = float(lines[i][3])
            else:
                dict_student_id_score[lines[i][0]] = {}
                dict_student_id_score[lines[i][0]][lines[i][1]] = float(lines[i][3])

        student_final_grade = {}
        policy = policy.read_policy()
        for key, values in dict_student_id_score.items():
            print(key, values)
            final_score = 0.0

            for k, v in values.items():
                if "Assignment" == k:
                    final_score += (v * float(policy.get("Assignment Weight"))) / (
                            100 * int(policy.get("Assignments Number")))
                elif "Test" == k:
                    final_score += (v * float(policy.get("Test Weight"))) / (100 * int(policy.get("Tests Number")))
                elif "FinalExam" == k:
                    final_score += (v * float(policy.get("Final Exam Weight"))) / (
                            100 * int(policy.get("Final Exam Number")))
            student_final_grade[key] = [values, str("Final score: ") + str(round(final_score, 2))]

        lines = list()
        with open('Student.csv', 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for i in range(len(lines)):
                    for k, v in student_final_grade.items():
                        if lines[i][0] == k:
                            remove_special1 = str.replace(str(v), "\'", '')
                            remove_special2 = str.replace(remove_special1, "[{", '')
                            update_line = [lines[i][0], lines[i][1], lines[i][2], remove_special2]
                            lines.remove(lines[i])
                            lines.append(update_line)

        with open('Grades.out.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)

        print("Successfully saved the student final grades to Grades.out.csv file")


def main():
    app = Policy()
    app.set_semester()
    app.write_policy()
    app.read_policy()


if __name__ == "__main__":
    main()
