from genericpath import exists
from hmac import new
import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email
        

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isloggedIn=False
        self.currentUser={}

        #load users from.json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists("users.json"):
            with open ("users.json","r",encoding="utf-8") as file:
                users=json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser=User(username=user["username"],password=user["password"],email=user["email"])
                    self.users.append(newUser)
                
                
    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("kullanıcı oluşturuşdu")
        
    
    def login(self,username,password):
        for user in self.users:
            if user.username== username and user.password==password:
                self.isloggedIn=True
                self.currentUser=user
                print("login yapıldı")
                break
            else:
                print("giriş yapılamadı:")
    
    def logOut(self):
        self.isloggedIn=False
        self.currentUser={}
        print("çıkış yapıldı")

    def identity(self):
        if self.isloggedIn:
            print(f"username: {self.currentUser.username}")
        else:
            print("giriş yapılmadı:")
    
    def savetoFile(self):
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))
        with open ('users.json',"w",encoding="utf-8") as file:
            json.dump(list,file)

repository=UserRepository()
while True:
    print("Menü".center(50,'*'))
    secim=input('1-Register\n2- Login\n3- Logout\n4- İdentity\n5- Exit\nSeçiminiz: ')
    if secim=="5":
        break
    else:
        if secim=="1":
            username=input("username: ")
            password=input("password: ")
            email= input("email: ")

            user=User(username=username,password=password,email=email)
            repository.register(user)
        elif secim=="2":
            username=input("username: ")
            password=input("password: ")

            repository.login(username,password)

        elif secim=="3":
            repository.logOut()
        elif secim =="4":
            repository.identity()
        else:
            print("yanlış seçim")
