# import math
# an = float(input('Digite o ângulo que você deseja: '))
# se = math.sin(math.radians(an))
# print('O ângulo de {} tem o SENO de {:.3f} '.format(an, se))
# cos = math.cos(math.radians(an))
# print('O ângulo de {} tem o COSSENO de {:.3f}'.format(an, cos))
# tag = math.tan(math.radians(an))
# print('A TANGENTE do ângulo {} é {:.3f}'.format(an, tag))

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
se = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.3f} '.format(an, se))
coss = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.3f}'.format(an, coss))
tag = tan(radians(an))
print('A TANGENTE do ângulo {} é {:.3f}'.format(an, tag))