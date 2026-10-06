'''Ask the user to input three numbers representing a lower limit, a higher limit, and a step value.
The program should use a range object to loop through and print the numbers from low to high (inclusive), taking into consideration the step.'''

lim_inf = int(input("Digite um limite inferior(valor inicial) "))
lim_sup = int(input("Digite um limite superior(valor final) "))
incr = int(input("Digite um valor de incremento "))
cont = lim_inf
if incr > 0 and lim_inf > lim_sup:
    print("Não é possível fazer uma contagem onde o incremento seja positivo e o limite inferior seja maior que o limite superior")
elif incr < 0 and lim_inf < lim_sup:
    print("Não é possível fazer uma contagem onde o incremento seja negativo e o limite inferior seja menor que o limite superior")
else:
    for i in range(lim_inf, lim_sup+int(incr / abs(incr)), incr):
        print(i)