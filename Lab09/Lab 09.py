# create a petstore class where you have the details of pets available and their details.
# The class will have methods
# -store a new pet details
# -search for a pet
# -sell a pet 
# -list all pets

# importing your petstore class,create a petstore to remain file, where you will implement a menu driven program for admin-who will manage the store & user who will manage the store and user who will see the pets and buy pets.
class petStore:
    def _init_(self):
        self.pets = {
            "Dog" : [],
            "Cat" : [],
            "Rabbit" : [],
            "Parrot" : []
        }
    def storePet(self,type,breedName,price,age):
        temp = {
            "breedName" : breedName,
            "price" : price,
            "age" : age,

        }
        self.pets[type].append(temp)
P=petStore()        
print(P.pets)
P.storePet("Dog","pomerian","5000","4")
print(P.pets)
P.storePet("Cat","persian","6000","3")
print(P.pets)
P.storePet("Dog","labrador","5500","4")
print(P.pets)
     
for i in P.pets:
    print(i)
    print(P.pets[i])
    for item in P.pets[i]:
        print(item["breedName"])

        