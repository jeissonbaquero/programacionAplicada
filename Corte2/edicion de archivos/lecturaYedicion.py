
#Se debe tener creado el archivos.text esto para abrir los en despues con el sigueite codigo
with open("Welcom.txt") as text_file:
    text_data= text_file.read()

#aqui leemos otro archivo 
with open ("how_many_lines.text") as line_doc:
    for line in line_doc.readlines():
        print(line)


#Posterioermete aquito en otro archuvo ejemplo lo eabrimos para escribir o editar sobre este
with open("bad_hands.txt","w") as bad_hands_doc:
    bad_hands_doc.write("Air buddy")

with open("cool_dogs.txt") as cool_dogs_file:
    cool_dogs_file.write("Perro de la cuadra")

with open("fun_file.txt") as file1:
    setup= file1.readline()
    punchline= file1.readline()
    print(setup)
    print(punchline)
    print(file1.readline())
