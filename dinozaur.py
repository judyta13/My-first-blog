print(1+1)
print ("hello, dajnozaur")
if 3>2:
    print ("to działa!")
if 5>2:
     print("5 jest jednak większe od 2")
else:
    print ("5 nie jest większe od 2")
zwierze = "dinozaur"
if zwierze == "kot":
    print ("Hej kot!")
elif zwierze == "dinozaur":
    print ("Hej dinozaur")
else:
    print ("hej niewiadomoco")
glosnosc = 57
if glosnosc < 20:
    print ("prawie nic nie slychac")
elif 20 <=glosnosc < 40:
    print ("o, muzyka leci w tle")
elif 40 <= glosnosc < 60:
    print ("super duper")
else:
    print ("scisz to!")
def hej ():
    print ("hej!")
    print ("czesc i czołem")

def hej (zwierze):
    if zwierze == "dinozaur":
        print ("hej dinozaur")
    elif zwierze == "kot":
        print ("hej kot")
    else:
        print ("hej niewiadomoco")
hej ("cos")
def hej (zwierze):
    print("hej " + zwierze + "!")
hej ("tygrysie")
hej ("zwierze")
print ("---------------")
dziewczyny = ["Ala","Tola",zwierze, "555"]
for imie in dziewczyny:
    imie.upper;
    hej(imie.upper())
