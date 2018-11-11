#
# -*- CODING UTF: 23 -*-
#
# -----------------------------------------
#
# -*- VICTOR HUGO -*-
#
# -----------------------------------------




nome = input("\t DIGITE SEU NOME: \n")

print("\t BEM VINDO",nome)

a = input("CALCULAR MÉDIA DO BOLETIM ----> \n'1'\n"
          "CALCULAR NOTA MÍNIMA NECESSÁRIA ----> \n'2'\n"
          "SAIR ----> \n'n'\n")


if a == 'n':
    print("\t OBRIGADO POR USAR MEU PROGRAMA",nome,"!!!\n")

    exit()


if a == '1':
    print("\t MÉDIA DO BOLETIM: \n")

    b = input(" \n'5'\n ----> MÉDIA DA ESCOLA 5"
              " \n'6'\n ----> MÉDIA DA ESCOLA 6"
              " \n'7'\n ----> MÉDIA DA ESCOLA 7")


    if b == '5':
        print("\t MÉDIA:5 \n")

        c = input("MÉDIA ANUAL ----> \n'1'\n"
                  "MÉDIA BIMESTRAL ----> \n'2'\n"
                  "MÉDIA SEMESTRAL ----> \n'3'\m")


        if c == '1':
            print("\t MÉDIA ANUAL: \n")

            
            d = input("PRESSIONE \n'1'\n PARA 4 BIMESTRES ANUAIS"
                      "PRESSIONE \n'2'\n PARA 2 SEMESTRES ANUAIS")

            if d == '1':
                print("\t 4 BIMESTRES ANUAIS: \n")

                e1 = input("DIGITE SUA MÉDIA DO 1º BIMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º BIMESTRE:")
                e3 = input("DIGITE SUA MÉDIA DO 3º BIMESTRE:")
                e4 = input("DIGITE SUA MÉDIA DO 4º BIMESTRE:")

                resp = (float(e1) + float(e2) + float(e3) + float(e4)) / 4

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")

            


            if d == '2':
                print("\t 2 SEMESTRES ANUAIS:\n")

                e1 = input("DIGITE SUA MÉDIA DO 1º SEMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º SEMESTRE:")

                resp = (float(e1) + float(e2)) /2

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")

            



            


            


        if c == '2':
            print("\t MÉDIA BIMESTRAL: \n")

            n = input("DIGITE O NÚMERO DE PROVAS POR BIMESTRE:")

            if n == '2':
                print("\t 2 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '3':
                print("\t 3 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '4':
                print("\t 4 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                





            


        if c == '3':
            print("\t MÉDIA SEMESTRAL: \n")

            x = input("DIGITE O NÚMERO DE PROVAS POR SEMESTRE: ")

            if x == '2':
                print("\t 2 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '3':
                print("\t 3 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA TRIMESTRAL É:",resp,"\n")


                


            if x == '4':
                print("\t 4 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\tSUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '5':
                print("\t 5 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e)) / 5

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                


            if x == '6':
                print("\t 6 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")
                f = input("DIGITE SUA NOTA NA 6º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e) + float(f)) / 6

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                



            


        


    if b == '6':
        print("\t MÉDIA:6 \n")

        c = input("MÉDIA ANUAL ----> \n'1'\n"
                  "MÉDIA BIMESTRAL ----> \n'2'\n"
                  "MÉDIA SEMESTRAL ----> \n'3'\m")


        if c == '1':
            print("\t MÉDIA ANUAL: \n")

            
            d = input("PRESSIONE \n'1'\n PARA 4 BIMESTRES ANUAIS"
                      "PRESSIONE \n'2'\n PARA 2 SEMESTRES ANUAIS")

            if d == '1':
                print("\t 4 BIMESTRES ANUAIS: \n")

                e1 = input("DIGITE SUA MÉDIA DO 1º BIMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º BIMESTRE:")
                e3 = input("DIGITE SUA MÉDIA DO 3º BIMESTRE:")
                e4 = input("DIGITE SUA MÉDIA DO 4º BIMESTRE:")

                resp = (float(e1) + float(e2) + float(e3) + float(e4)) / 4

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")

                


            if d == '2':
                print("\t 2 SEMESTRES ANUAIS:\n")

                e1 = input("DIGITE SUA MÉDIA DO 1º SEMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º SEMESTRE:")

                resp = (float(e1) + float(e2)) /2

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")

                




            


        if c == '2':
            print("\t MÉDIA BIMESTRAL: \n")

            n = input("DIGITE O NÚMERO DE PROVAS POR BIMESTRE:")

            if n == '2':
                print("\t 2 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '3':
                print("\t 3 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '4':
                print("\t 4 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


            



            


        if c == '3':
            print("\t MÉDIA SEMESTRAL: \n")

            x = input("DIGITE O NÚMERO DE PROVAS POR SEMESTRE: ")

            if x == '2':
                print("\t 2 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '3':
                print("\t 3 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA TRIMESTRAL É:",resp,"\n")


                


            if x == '4':
                print("\t 4 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\tSUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '5':
                print("\t 5 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e)) / 5

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                


            if x == '6':
                print("\t 6 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")
                f = input("DIGITE SUA NOTA NA 6º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e) + float(f)) / 6

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                




            

        


    if b == '7':
        print("\t MÉDIA:7 \n")

        c = input("MÉDIA ANUAL ----> \n'1'\n"
                  "MÉDIA BIMESTRAL ----> \n'2'\n"
                  "MÉDIA SEMESTRAL ----> \n'3'\m")


        if c == '1':
            print("\t MÉDIA ANUAL: \n")

            
            d = input("PRESSIONE \n'1'\n PARA 4 BIMESTRES ANUAIS"
                      "PRESSIONE \n'2'\n PARA 2 SEMESTRES ANUAIS")

            if d == '1':
                print("\t 4 BIMESTRES ANUAIS: \n")

                e1 = input("DIGITE SUA MÉDIA DO 1º BIMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º BIMESTRE:")
                e3 = input("DIGITE SUA MÉDIA DO 3º BIMESTRE:")
                e4 = input("DIGITE SUA MÉDIA DO 4º BIMESTRE:")

                resp = (float(e1) + float(e2) + float(e3) + float(e4)) / 4

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")

                


            if d == '2':
                print("\t 2 SEMESTRES ANUAIS:\n")

                e1 = input("DIGITE SUA MÉDIA DO 1º SEMESTRE:")
                e2 = input("DIGITE SUA MÉDIA DO 2º SEMESTRE:")

                resp = (float(e1) + float(e2)) /2

                print("\t SUA MÉDIA ANUAL É:",resp,"\n")




            


        if c == '2':
            print("\t MÉDIA BIMESTRAL: \n")

            n = input("DIGITE O NÚMERO DE PROVAS POR BIMESTRE:")

            if n == '2':
                print("\t 2 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '3':
                print("\t 3 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                


            if n == '4':
                print("\t 4 PROVAS POR BIMESTRE: \n")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\t SUA MÉDIA BIMESTRAL É:",resp,"\n")


                




            


        if c == '3':
            print("\t MÉDIA SEMESTRAL: \n")

            x = input("DIGITE O NÚMERO DE PROVAS POR SEMESTRE: ")

            if x == '2':
                print("\t 2 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")

                resp = (float(a) + float(b)) / 2

                print("\t SUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '3':
                print("\t 3 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")

                resp = (float(a) + float(b) + float(c)) / 3

                print("\t SUA MÉDIA TRIMESTRAL É:",resp,"\n")


                


            if x == '4':
                print("\t 4 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d)) / 4

                print("\tSUA MÉDIA SEMESTRAL É:",resp,"\n")


                


            if x == '5':
                print("\t 5 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e)) / 5

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                


            if x == '6':
                print("\t 6 PROVAS POR SEMESTRE: ")

                a = input("DIGITE SUA NOTA NA 1º PROVA: ")
                b = input("DIGITE SUA NOTA NA 2º PROVA: ")
                c = input("DIGITE SUA NOTA NA 3º PROVA: ")
                d = input("DIGITE SUA NOTA NA 4º PROVA: ")
                e = input("DIGITE SUA NOTA NA 5º PROVA: ")
                f = input("DIGITE SUA NOTA NA 6º PROVA: ")

                resp = (float(a) + float(b) + float(c) + float(d) + float(e) + float(f)) / 6

                print("\t SUA MÉDIA SEMESTRAL É:",resp," \n")


                




            

        


if a == '2':
    print("\t CALCULAR NOTA MÍNIMA NECESSÁRIA: \n")

    x = input("NOTA NECESSÁRIA ANUAL ----> \n'1'\n"
              "NOTA NECESSÁRIA BIMESTRAL ----> \n'2'\n"
              "NOTA NECESSÁRIA SEMESTRAL ----> \n'3'\n"
              "SAIR ----> \n'n'\n")


    if x == 'n':
        print("\t OBRIGADO POR USAR MEU PROGRAMA",nome,"\n")

        exit()


    if x == '1':
        print("\t NOTA NECESSÁRIA ANUAL: \n")

        b = input("PRESSIONE \n'1'\n PARA 4 BIMESTRES ANUAIS"
                  "PRESSIONE \n'2'\n PARA 2 SEMESTRES ANUAIS")


        if b == '1':
            print("\t 4 BIMESTRES ANUAIS: \n")

            c = input("DIGITE A MÉDIA DE SUA ESCOLA: ")
            d = input("DIGITE SUA NOTA DO 1º BIMESTRE: ")
            e = input("DIGITE SUA NOTA DO 2º BIMESTRE: ")
            f = input("DIGITE SUA NOTA DO 3º BIMESTRE: ")
            g = input("DIGITE SUA NOTA DO 4º BIMESTRE: ")
            h = input("DIGITE PONTOS EXTRAS: (se não houver, digite 0)")

            media = float(c) * 4

            resp =    media - (float(d) + float(e) + float(f) + float(g) + float(h))

            print("\t FALTAM:",resp," PoNTOS PARA VOCÊ PASSAR \n")

            print("obs.: se sua resposta foi um número negativo, você já atingiu a média necessária")


            


        if b == '2':
            print('\t 2 SEMESTRES ANUAIS: \n')

            a = input("DIGITE A MÉDIA DE SUA ESCOLA: ")
            b = input("DIGITE A NOTA DO 1º SEMESTRE: ")
            c = input("DIGITE A NOTA DO 2º SEMESTRE: ")
            d = input("DIGITE PONTOS EXTRAS: (se não houver, digite 0)")

            media = float(a) * 2

            resp = media - (float(b) + float(c) + float(d))

            print("\t FALTAM:",resp," PONTOS PARA VOCÊ PASSAR \n")

            print("obs.: se sua resposta foi um número negativo, você já atingiu a média necessária ")


            




    if x == '2':
        print("\t NOTA NECESSÁRIA BIMESTRAL: \n")

        a = input("DIGITE A MÉDIA DE SUA ESCOLA: ")
        b = input("DIGITE A NOTA DA 1º PROVA: ")

        resp = float(a) - (float(b) / 2)

        print("\t FALTAM:",resp," PONTOS PARA VOCÊ PASSAR \n")

        print("obs.: se sua resposta foi um número negativo, você já atingiu a média necessária")

        


    if x == '3':
        print("\t NOTA NECESSÁRIA SEMESTRAL: \n")

        a = input("PRESSIONE \n'1'\n PARA SEMESTRE COM 3 PROVAS"
                  "PRESSIONE \n'2'\n PARA SEMESTRE COM 4 PROVAS")


        if a == '1':
            print("\t SEMESTRE COM 3 PROVAS: \n")

            n = input("DIGITE A MÉDIA DE SUA ESCOLA: ")
            m = input("DIGITE SUA NOTA NA 1º PROVA: ")
            o = input("DIGITE SUA NOTA NA 2º PROVA: ")

            resp =  float(n) - ((float(m) + float(o)) / 2)

            print("\t FALTAM:",resp," PONTOS PARA VOCÊ PASSAR \n")

            print("obs.: se sua resposta foi um número negativo, você já atingiu a média necessária")


            


        if a == '2':
            print("\t SEMESTRE COM 4 PROVAS: \n")

            a = input("DIGITE A MÉDIA DE SUA ESCOLA: ")
            b = input("DIGITE SUA NOTA NA 1º PROVA: ")
            c = input("DIGITE SUA NOTA NA 2º PROVA: ")
            d = input("DIGITE SUA NOTA NA 3º PROVA: ")

            resp = float(a) - ((float(b) + float(c) + float(d)) / 3)

            print("\t FALTAM:",resp," PONTOS PARA VOCÊ PASSAR \n")

            print("obs.: se sua resposta foi um número negativo, você já atingiu a média necessária")


            








# -----------------------------------------------------
#
# -*- VICTOR HUGO -*-
#
# -----------------------------------------------------
