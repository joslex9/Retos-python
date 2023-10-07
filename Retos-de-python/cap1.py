try:
    dia = input('Digite el dia de la semana que fue a playa:  ')
    horas = int(input('Horas en el estacionamiento: '))
    minutos = int(input('Digite los minutos: '))
    
    d_v = ['lunes', 'martes', 'miercoles','jueves','viernes','sabado','domingo']
    if dia.lower() in d_v and 0 <= minutos <= 59 and horas >= 0:
        if horas >= 1 or minutos >= 6:
            if minutos >= 6:
                minutos = 1
            else: 
                minutos = 0

            if dia.lower()  in ['lunes', 'martes', 'miercoles']:
                valor = 2.00*(horas + minutos)
                print(f'valor a pagar {valor}')
            elif dia.lower()  in ['jueves','viernes']:
                valor = 2.50*(horas + minutos)
                print(f'valor a pagar {valor}')
            elif dia.lower()  in ['sabado','domingo']:
                valor = 3.00*(horas + minutos)
                print(f'valor a pagar {valor}')
        else:
            print('Su estacionamiento es gratis:')
    else:
        print('valor incorrecto')            
        

except ValueError:
    print('valor incorrecto')