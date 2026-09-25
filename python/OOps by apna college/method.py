#  instance method

# class Employee:
#     def __init__(self,side):
#         self.side =side

#     def square(self):
#         area=self.side*self.side
#         print("the area is : ",area)

# e=Employee(20)
# e.square()


# class method

class Language:

    

    @classmethod
    def changeLanguage(cls, language):
        cls.common_language = language
        print("Common language:", cls.common_language)

    def language(self):
        different_lang = "Telugu"
        print("Here language is:", different_lang)


l = Language()

Language.changeLanguage("English")
l.language()
   


#  static method
class Student:

    @staticmethod
    def isPass(marks):
        if marks >= 40:
            return "Pass"
        else:
            return "Fail"

print(Student.isPass(75))


