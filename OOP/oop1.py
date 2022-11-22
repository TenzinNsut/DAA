

class PascalCase:
    def __init__(self, name, age ,country):
        self.person_name = name
        self.person_age =  age
        self.person_country = country

    def __repr__(self):
        return "hello world"

    def __str__(self):
        return f"Person: {self.person_name} age: {self.person_age} country: {self.person_country}"


p1 = PascalCase("Tenzin",19,"India")
p2 = PascalCase("Rick",20,"United States")

print(p1)
print(p2)