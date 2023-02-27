import random
import datetime
import json

N_RECORDS = 100
FILE_NAME = 'generated_sample_data.json'
DATE_FORMAT = '%Y-%m-%d'


def generate_sample_data(n, file_name):
    students = ['alice', 'adam', 'bob', 'brian', 'charlie']
    courses = ['algorithms', 'datastructures', 'security', 'oop', 'databases']
    subscribed_at = datetime.datetime.now()
    generated_sample_data_list = []
    for i in range(n):
        student = random.choice(students)
        course = random.choice(courses)
        subscribed_at = subscribed_at + datetime.timedelta(days=random.randint(1, 10))
        print(f'student: {student} | course: {course} | subscribed_at: {subscribed_at.strftime(DATE_FORMAT)}')
        generated_sample_data_list.append({'student': student, 'course': course, 'subscribed_at': subscribed_at.strftime(DATE_FORMAT)})

    with open(file_name, 'w') as f:
        f.write(json.dumps(generated_sample_data_list, indent=None, separators=(',', ':')).replace('},', '},\n'))


if __name__ == '__main__':
    generate_sample_data(N_RECORDS, FILE_NAME)
