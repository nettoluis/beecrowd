1061
'''Indicar a duração de um evento contendo informações dos dias, horas, minutos e segundos expendidos durante esse período'''
#Coletando os dados brutos
diaDeInicio,horarioDeInicio, diaDeTermino, horarioDeTermino = input(), list(input().split(' : ')), input(), list(input(). split(' : '))
#Refinando os dados do início do evento
diaInicial,horaInicial ,minutoInicial, segundoInicial = int(diaDeInicio[4:]), int(horarioDeInicio[0]), int(horarioDeInicio[1]), int(horarioDeInicio[2])
#Refinando os dados do término do evento
diaFinal, horaFinal, minutoFinal, segundoFinal = int(diaDeTermino[4:]), int(horarioDeTermino[0]), int(horarioDeTermino[1]), int(horarioDeTermino[2])
#Cálculos
segundosIniciais, segundosFinais = (diaInicial * 86400) + (horaInicial * 3600) + (minutoInicial * 60) + segundoInicial, (diaFinal * 86400) + (horaFinal * 3600) + (minutoFinal * 60) + segundoFinal
segundosDecorridos = segundosFinais - segundosIniciais
duracaoEmDias, duracaoEmHoras, duracaoEmMinutos, duracaoEmSegundos = segundosDecorridos // 86400,(segundosDecorridos % 86400) // 3600, (segundosDecorridos % 3600) // 60, (segundosDecorridos % 60)
#Output do resultado
print(f'{duracaoEmDias} dia(s)')
print(f'{duracaoEmHoras} hora(s)')
print(f'{duracaoEmMinutos} minuto(s)')
print(f'{duracaoEmSegundos} segundo(s)')
