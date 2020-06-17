#Incomplete:
hotdogsInPackage=10
hotdogsInbuns=8
numberOfPeople=int(input("Enter number of people attending the coockout:"))
hotDogs=int(input("Enter number of hotdogs required:"))
hotDogsBuns=int(input("Enter number of hotdogs buns required:"))
hotDogsNeeded=hotDogs*numberOfPeople
hotDogsBunsNeeded=hotDogsBuns*numberOfPeople
exacthotdogspackages=hotDogsNeeded/hotdogsInPackage
exacthotDogsBunsNeeded=hotDogsBunsNeeded/hotdogsInbuns
hotdogspackagesRemender=hotDogsNeeded%hotdogsInPackage
hotdogsInbunsRemender=hotDogsBunsNeeded%hotdogsInbuns
if hotdogspackagesRemender>0:
    minimumHotpackageRequired=int(exacthotdogspackages+1)
else:
    minimumHotpackageRequired=exacthotdogspackages
if hotdogsInbunsRemender>0:
    miniumhotdogbunrequired=int(exacthotdogspackages+1)
else:
    miniumhotdogpackagesrequired=exacthotdogspackages

