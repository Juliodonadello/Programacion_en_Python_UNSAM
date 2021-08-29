# hipoteca.py

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto = 1000
inicio_adelanto = 61
fin_adelanto= 108
meses=0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    meses+=1

    if meses >= inicio_adelanto and meses<=fin_adelanto:        
        saldo -= adelanto
        total_pagado += adelanto

    
    
    if saldo<0:
        total_pagado+=saldo
        saldo=0
        print(meses, round(total_pagado, 2), round(saldo, 2))
        break

    print(meses, round(total_pagado, 2), round(saldo, 2))


print('Total pagado', round(total_pagado, 2))
print("Meses: ", meses)