def comparar_data(data1, data2):
    if data1 > data2:
        print("Data 1 é mais recente.")
    elif data1 < data2:
        print("Data 2 é mais recente.")
    else:
        print("As datas são iguais.")

data1 = (2024,5,18)
data2 = (2025,8,20)

comparar_data(data1,data2)