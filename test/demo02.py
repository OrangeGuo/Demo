class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_info(self):
        print('%s : %s' % (self.name, self.score))

Mary = Student('Mary', 99)
David = Student('David', 80)

Mary.print_info()
David.print_info()