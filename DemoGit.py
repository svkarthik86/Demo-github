class Students:
    stdName = ""
    stdRegNo = ""
    stdadd = ""
    def set_value(self, name, regno, add):
        self.stdName = name
        self.stdRegNo = regno
        self.stdadd = add
    def display(self):
        print("Name:"+self.stdName + " " + "RegNo:" + self.stdRegNo + " " + "Address:" + self.stdadd)
s1 = Students()
s1.display()
s1.set_value("Jhon", "1002", "Bangalore")
s1.display()
s2=Students()
s2.set_value("Ram","1003","chennai")
s2.display()
