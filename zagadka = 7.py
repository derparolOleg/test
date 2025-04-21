predlogenie = input("введите предложение ")
ploxie_clova = ["лох" , "плохой"]
for i in ploxie_clova:
    if i in predlogenie:
        print("найдено плохое слово")
        break
    else:
        print("все впорядке")