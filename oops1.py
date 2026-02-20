class employee:
    def __init__(self):
        self.__name="sameer"
        self.id= 1821202025
        self.salary= 50000
        self.designation="SDE"

    def travel(self,destination):
        print("check travel")
        print(f"empoloyee is now travelling to {destination}")

sam=employee()
sam.name= "Sameer"
shaktiman=employee()
print(sam.name)
print(id(shaktiman))
sam.travel("Chennai")

#print(type(sam))