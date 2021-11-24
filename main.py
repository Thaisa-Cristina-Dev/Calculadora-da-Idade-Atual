from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date


janela = Tk()
janela. title("Calculadora da Idade")
janela.geometry('310x400')

#cores
cor1= "#3b3b3b" #preto leve
cor2= "#333333" # preto forte
cor3= "#ffffff" # branco
cor4= "#fcc058"  # laranja

#criando frames

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#criando labes para frame cima

l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor='center', font=('Ivi 15 bold'), bg=cor2, fg=cor3)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor='center', font=('Arial 35 bold'), bg=cor2, fg=cor4)
l_idade.place(x=0, y=70)


#funcao calcular idade

def calcular():
    inicial = cal_1.get()
    termino = cal_2.get()

    #separando os valores
    mes_1, dia_1, ano_1 = [int(f) for f in inicial.split('/')]
    
    #convertendo os valores em formato date
    data_inicial = date(ano_1, mes_1, dia_1)

    #separando os valores
    mes_2, dia_2, ano_2 = [int(f) for f in termino.split('/')]

    #convertendo os valores em formato date/datetime
    data_nascimento = date(ano_2, mes_2, dia_2)
    
    anos =relativedelta(data_inicial, data_nascimento).years
    meses =relativedelta(data_inicial, data_nascimento).months
    dias =relativedelta(data_inicial, data_nascimento).days

    print()
    
    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias

#criando labes para frame baixo

l_data_inicial = Label(frame_baixo, text="Data Inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11 '), bg=cor2, fg=cor3)
l_data_inicial.place(x=50, y=30)


cal_1 = DateEntry(frame_baixo, Width=13, bg='darkblue', fg=cor3, boderwith=2, date_pattern = 'mm/dd/y', y=2021)
cal_1.place(x=180, y=30)  


l_data_nascimento = Label(frame_baixo, text="Data de Nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11 '), bg=cor2, fg=cor3)
l_data_nascimento.place(x=40, y=70)

cal_2 = DateEntry(frame_baixo, Width=13, bg='darkblue', fg=cor3, boderwith=2, date_pattern = 'mm/dd/y', y=2021)
cal_2.place(x=180, y=70)




l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 20 bold '), bg=cor1, fg=cor3)
l_app_anos_nome.place(x=50, y=175)  


l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 20 bold '), bg=cor1, fg=cor3)
l_app_meses_nome.place(x=130, y=175)

l_app_dias = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 25 bold '), bg=cor1, fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief=FLAT, anchor='center', font=('Ivi 20 bold '), bg=cor1, fg=cor3)
l_app_dias_nome.place(x=220, y=175)


#criando botão calcular

b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=20, height=1, relief=RAISED, overrelief='ridge', font=('Ivi 10 bold '), bg=cor1, fg=cor3)
b_calcular.place(x=70, y=225)


janela.mainloop()


