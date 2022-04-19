#!/usr/bin/env python
# coding: utf-8

# # Balanceo de ecuaciones químicas:
# MSc. Jesus Alvarado-Huayhuaz
# #### __Rxn de combustión de hidrocarburos__

# ##### __Combustión de Alcanos__
# a $C_nH_{2n+2}$ + b $O_2$ = c $CO_2$ + d $H_2O$
# 
# ##### __Combustión de Alquenos__
# a $C_nH_{2n}$ + b $O_2$ = c $CO_2$ + d $H_2O$
# 
# ##### __Combustión de Alquinos__
# a $C_nH_{2n-2}$ + b $O_2$ = c $CO_2$ + d $H_2O$

# In[1]:


print("REACCIÓN DE COMBUSTIÓN DE")
print('--------------------------------')
print('    1. Alcanos\n    2. Alquenos\n    3. Alquinos')
print('--------------------------------')

rxn = int(input('Indica el tipo de hidrocarburo: 1, 2 o 3: '))
while (rxn != 1) and (rxn != 2) and (rxn != 3):
    print("¡Ha escrito un número inválido! Inténtelo de nuevo")
    rxn = int(input('Indica el tipo de hidrocarburo: 1, 2 o 3: '))

#**********************************************************************************
#función para usar subindice  
def get_sub(x): 
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s)) 
    return x.translate(res) 
#**********************************************************************************
    
if rxn == 1:
    print(' ')
    print('[Combustión de Alcanos]')
    print('a C{}H{} + b O{} = c CO{} + d H{}O'.format(get_sub('n'),get_sub('2n+2'),get_sub('2'),get_sub('2'),get_sub('2')))
elif rxn == 2:
    print(' ')
    print('[Combustión de Alquenos]')
    print('a C{}H{} + b O{} = c CO{} + d H{}O'.format(get_sub('n'),get_sub('2n'),get_sub('2'),get_sub('2'),get_sub('2')))
elif rxn == 3:
    print(' ')
    print('[Combustión de Alquinos]')
    print('a C{}H{} + b O{} = c CO{} + d H{}O'.format(get_sub('n'),get_sub('2n-2'),get_sub('2'),get_sub('2'),get_sub('2')))


# In[2]:


if rxn == 1: 
    carbonos = int(input('Indica el número de carbonos en el alcano: '))
    a = 1
    b = (3*carbonos+1)/2
    c = carbonos
    d = carbonos+1
    print(' ')
    print('---ECUACIÓN BALANCEADA---')
    print('C{}H{} + {} O{} = {} CO{} + {} H{}O'.
          format(get_sub(str(carbonos)),get_sub(str(2*carbonos+2)),str(b),
                 get_sub('2'),str(c),get_sub('2'),str(d),get_sub('2')))
    
if rxn == 2: 
    carbonos = int(input('Indica el número de carbonos en el alqueno: '))
    a = 1
    b = (3*carbonos)/2
    c = carbonos
    d = carbonos
    print(' ')
    print('---ECUACIÓN BALANCEADA---')
    print('C{}H{} + {} O{} = {} CO{} + {} H{}O'.
          format(get_sub(str(carbonos)),get_sub(str(2*carbonos)),str(b),
                 get_sub('2'),str(c),get_sub('2'),str(d),get_sub('2')))
    
if rxn == 3: 
    carbonos = int(input('Indica el número de carbonos en el alquino: '))
    a = 1
    b = (3*carbonos-1)/2
    c = carbonos
    d = carbonos-1
    print(' ')
    print('---ECUACIÓN BALANCEADA---')
    print('C{}H{} + {} O{} = {} CO{} + {} H{}O'.
          format(get_sub(str(carbonos)),get_sub(str(2*carbonos-2)),str(b),
                 get_sub('2'),str(c),get_sub('2'),str(d),get_sub('2')))


# In[ ]:




