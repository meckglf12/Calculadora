

def formula(valor1,valor2,valor3) :
    if valor3 == '+':
        x = valor1 + valor2
        return int(x)
    
    elif valor3 == '-' :
        x = valor1 - valor2
        return int(x)
    
    elif valor3 == '*' :
        x = valor1 * valor2
        return int(x)
    
    elif valor3 == '/' :
        x = valor1 / valor2
        return int(x)
    
    else : 
        return 'Sinal não aceito'

lista = []
simbolo = ''
total = 0

while simbolo != '=':
    
    
    numero = input('numero 1 : ')
    if numero   == '=':
        break    
    
    numerodois = input('numero 2 : ')
    if numerodois   == '=':
        lista.append(int(numero))
        break    
        
    simbolo = input('sinal ')

    if simbolo   == '=':
        lista.append((int(numero),int(numerodois)))
        break    
    else:
        
        total = (formula(int(numero),int(numerodois),simbolo))
        lista.append(int(total)) 

for item in lista :
    print(item)


