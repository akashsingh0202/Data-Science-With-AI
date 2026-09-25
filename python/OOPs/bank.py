class bank:

  def __init__(self,name,age,pin): #instance variables / attributes
    self.name = name
    self.age = age
    self.pin = pin

  def get_info(self): #getter methods
    print(self.name,self.age,self.pin)



a = bank('Ajay',22,1234) #object creation
b = bank('rahul',45,3456)