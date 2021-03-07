class Researcher:

    def __init__(self, field):
        self.field = field

    def __str__(self):
        return "Research field: "+self.field+"\n"


class Teacher:

    def __init__(self, courses_list):
        self.courses_list = courses_list

    def __str__(self):
        out = "Courses: "
        for c in self.courses_list:
            out += c+", " 

        return out[:-2]+"\n"


class Professor(Teacher, Researcher):

    def __init__(self, name, field, course_list):

        Researcher.__init__(self, field)
        Teacher.__init__(self, course_list)
        self.name = name

    def __str__(self):
        out = Researcher.__str__(self)
        out += Teacher.__str__(self)
        out += "Name: " + self.name + "\n"
        return out


if __name__ == "__main__":

    p = Professor("Steve Iams",
            "Machine Learning", 
            [
                "Python Programming",
                "Probabilistic Graphical Models",
                "Bayesian Inference"
                ])
    print(p)
