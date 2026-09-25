class employee:
    lang="python"
    salary=120000

    def getInfo(self):
        print(f"the laanguage is {self.lang} and his salary is {self.salary}")

s=employee()
s.lang="javasscript"

s.getInfo()