class StudentInfoError(Exception):
    def __init__(self, message):
        self.message = message

def find_ID(name, info):
    if name in info:
        return info[name]
    raise StudentInfoError("Student ID not found for " + name)

def find_name(ID, info):
    for name in info:
        if ID == info[name]:
            return name
    raise StudentInfoError("Student name not found for " + ID)

if __name__ == "__main__":
    student_info = {
        "Reagan" : "rebradshaw835",
        "Ryley" : "rbarber894",
        "Peyton" : "pstott885",
        "Tyrese" : "tmayo945",
        "Caius" : "ccharlton329"
    }

    print("Enter the users ID or name: ")
    userChoice = input()

    try:
        if userChoice == "0":
            name = input()
            result = find_ID(name, student_info)
        else:
            ID = input()
            result = find_name(ID, student_info)
        print(result)
    except StudentInfoError as excpt:
        print(excpt)
