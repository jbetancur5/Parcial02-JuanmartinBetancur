from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/factorial/<int:number>')
def factorial(number):
    # Calcula el factorial del número recibido en la URL
    result = 1
    for i in range(1, number + 1):
        result *= i
    return render_template_string(f"<h1>Factorial de {number} es {result}</h1>")

if __name__ == '__main__':
    app.run(debug=True)



#Para visualizar el factorial:
#Correr el proyecto en la url debe el poner url/factorial/#