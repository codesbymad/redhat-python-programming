'''Write an application that prompts to enter the radius of a circle.
Accept the user input into a variable.
Compute and print the area of the circle whose radius was input.
The formula for the area of a circle is πr² (pi times the square of the radius).
Use 3.14159 for pi.'''

raio = int(input("Digite o raio "))
area = 3.14159 * (raio ** 2)
print(f"A area do circulo de raio {raio} é {area}")