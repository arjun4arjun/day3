class employee:
    def __init__(self):
        print("check1")
        self.id= 1821202025
        self.salary= 50000
        self.designation="SDE"
        print("check2")
    def travel(self,destination):
        print("check travel")
        print(f"empoloyee is now travelling to {destination}")

sam=employee()
#print(sam.id)
sam.travel("Chennai")

print(type(sam))