def getStudentOfTheDay():
    return {
        "firstName": "Aakash",
        "lastName": "Appalaneni",
        "studentGrade": "6"
    }


def printStudentInfo(functionToBeDecorated):
    def studentDecoratorOther(*args):
        student = functionToBeDecorated(*args)
        print(
            f'First name: {student["firstName"]}, last name = {student["lastName"]}, student grade: {student["studentGrade"]} ')
        return student

    return studentDecoratorOther


def printStudentInfoOther(functionToBeDecorated):
    def studentDecorator(*args):
        student = functionToBeDecorated(*args)
        print(
            f'Last name: {student["lastName"]}, first name = {student["firstName"]}, student grade: {student["studentGrade"]} ')
        return student

    return studentDecorator


decoratorStudentInfo = printStudentInfo(getStudentOfTheDay)
decoratorStudentInfo()
print("--------------------------------------------------------------------------------------------------------------")
decoratorStudentInfoOther = printStudentInfoOther(getStudentOfTheDay)
decoratorStudentInfoOther()
