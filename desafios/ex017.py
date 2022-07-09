# op = float(input('Digite o comprimento do cateto oposto: '))
# ad = float(input('Digite o comprimento do cateto adjacente: '))
# hi = (op ** 2 + ad ** 2) ** (1/2)
# print('A hipotenusa vai medir {:.2f}'.format(hi))

import math
op = float(input('Digite o cumprimento do cateto oposto: '))
ad = float(input('Digite o cumprimento do cateto adjacente: '))
hi = math.hypot(op, ad)
print('A hipotenusa vai medir {:.2f}'.format(hi))


# form math import hypot
# op = float(input('Digite o cumprimento do cateto oposto: '))
# ad = float(input('Digite o cumprimento do cateto adjacente: '))
# hi = hypot(op, ad)
# print('A hipotenusa vai medir {:.2f}'.format(hi))