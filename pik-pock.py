import random

print("=== PIK POCK ===")
print("1. Tosh Qaychi Qog'oz")
print("2. Son topish")
print("3. X O")
print("4. Kalkulyator")
print("5. Tanga tashlash")
print("6. Zar tashlash")
print("7. Chiqish")

tanlov = input("Tanlang: ")

if tanlov == "1":
    variantlar = ["Tosh", "Qaychi", "Qog'oz"]
    siz = input("Tosh/Qaychi/Qog'oz: ").capitalize()
    kom = random.choice(variantlar)

    print("Kompyuter:", kom)

    if siz == kom:
        print("🤝 Durrang")
    elif (siz == "Tosh" and kom == "Qaychi") or \
         (siz == "Qaychi" and kom == "Qog'oz") or \
         (siz == "Qog'oz" and kom == "Tosh"):
        print("🏆 Siz yutdingiz")
    else:
        print("💻 Kompyuter yutdi")

elif tanlov == "2":
    sir = random.randint(1, 10)

    while True:
        son = int(input("1-10 son kiriting: "))

        if son == sir:
            print("🎉 Topdingiz!")
            break
        elif son < sir:
            print("📈 Kattaroq son kiriting")
        else:
            print("📉 Kichikroq son kiriting")
    print("⭕ X O")

    doska = ["1","2","3",
             "4","5","6",
             "7","8","9"]

    while True:
        print()
        print(doska[0], "|", doska[1], "|", doska[2])
        print("--+---+--")
        print(doska[3], "|", doska[4], "|", doska[5])
        print("--+---+--")
        print(doska[6], "|", doska[7], "|", doska[8])

        tanla = int(input("Katak (1-9): "))

        if tanla < 1 or tanla > 9:
            print("Xato!")
            continue

        if doska[tanla-1] in ["X","O"]:
            print("Band!")
            continue

        doska[tanla-1] = "X"

        bosh = []
        for i in range(9):
            if doska[i] not in ["X","O"]:
                bosh.append(i)

        if len(bosh) > 0:
            kom = random.choice(bosh)
            doska[kom] = "O"

        if all(i in ["X","O"] for i in doska):
            print("🤝 O'yin tugadi")
            break

elif tanlov == "4":
    print("🧮 Kalkulyator")

    a = float(input("1-son: "))
    amal = input("+  -  *  / : ")
    b = float(input("2-son: "))

    if amal == "+":
        print(a+b)
    elif amal == "-":
        print(a-b)
    elif amal == "*":
        print(a*b)
    elif amal == "/":
        if b != 0:
            print(a/b)
        else:
            print("0 ga bo'linmaydi")
           
    print("\n🪙 Tanga tashlash")

    natija = random.choice(["Gerb", "Raqam"])
    print("Natija:", natija)

elif tanlov == "6":
    print("\n🎲 Zar tashlash")

    print("Zar tushdi:", random.randint(1, 6))

elif tanlov == "7":
    print("\n👋 Dastur tugadi.")

else:
    print("❌ Noto'g'ri tanlov!")
    print("=== PIK POCK ===")
print("1. Tosh Qaychi Qog'oz")
print("2. Son topish")
print("3. X O")
print("4. Kalkulyator")
print("5. Tanga tashlash")
print("6. Zar tashlash")
print("7. Chiqish")
