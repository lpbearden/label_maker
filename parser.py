import csv, os, re
from constants import GRADE_MAP

# for root, subdirs, files in os.walk(os.getcwd()):
classes = dict()

for file in os.listdir('classes'):
    if file.endswith('.csv'):
        teacher_name = os.path.splitext(file)[0].split()[0] + '.' + ' ' + os.path.splitext(file)[0].split()[1]
        class_list = list()
        with open(os.path.join('classes', file), 'r', encoding='utf-8-sig') as fin:
            reader = csv.reader(fin, delimiter=',')
            for row in reader:
                if re.search('[a-zA-Z]', row[0]):
                    if len(row[0].split()) > 2:
                        student_name = row[0].split()[2] + ' ' + row[0].split()[0][0] + '.'
                    else:
                        student_name = row[0].split()[1] + ' ' + row[0].split()[0][0] + '.'
                    class_list.append(student_name)
            classes[teacher_name] = class_list

with open('test_run.csv', mode='w') as test_run:
    test_writer = csv.writer(test_run, delimiter=',', quotechar='"')
    for teacher in classes:
        grade = GRADE_MAP[teacher] + ' Grade'
        print (teacher)
        for i in range(0, len(classes[teacher]), 4):
            print('index', i, 'list size', len(classes[teacher]))
            if len(classes[teacher]) - 1 >= i+3:
                test_writer.writerow([classes[teacher][i], classes[teacher][i+1], classes[teacher][i+2], classes[teacher][i+3]])
                test_writer.writerow([teacher, teacher, teacher, teacher])
                test_writer.writerow([grade, grade, grade, grade])
                test_writer.writerow([''])

            elif len(classes[teacher]) - 1 >= i+2:
                test_writer.writerow([classes[teacher][i], classes[teacher][i+1], classes[teacher][i+2]])
                test_writer.writerow([teacher, teacher, teacher])
                test_writer.writerow([grade, grade, grade])
                test_writer.writerow([''])

            elif len(classes[teacher]) - 1 >= i+1:
                test_writer.writerow([classes[teacher][i], classes[teacher][i+1]])
                test_writer.writerow([teacher, teacher])
                test_writer.writerow([grade, grade])
                test_writer.writerow([''])

            elif len(classes[teacher]) - 1 >= i:
                test_writer.writerow([classes[teacher][i]])
                test_writer.writerow([teacher])
                test_writer.writerow([grade])
                test_writer.writerow([''])
