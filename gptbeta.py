import openai
import time

# Se establece la clave de API de OpenAI
openai.api_key = "api-key"

# Se define el modelo de lenguaje GPT-3 a utilizar
engine_model_gpt3 = "text-davinci-003"

# Se define el tiempo máximo de espera para obtener la respuesta del modelo
WAIT_TIME = 10

# Se define una función para obtener la entrada del usuario de manera segura
def get_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        return None

# Se define una función para generar texto a partir de una entrada dada por el usuario
def generate_text(prompt, engine, max_tokens=1024, n=1, stop=None, temperature=0.2):
    try:
        # Se crea la solicitud de generación de texto
        completion = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            n=n,
            stop=stop,
            temperature=temperature
        )
        # Se devuelve el texto generado por el modelo
        return completion.choices[0].text
    except openai.error.APIError as e:
        # Si se produce un error en la API, se muestra un mensaje de error en la pantalla
        print(f"OpenAI API error: {e}")
        return None

# Se define una función para ejecutar el programa principal
def main():
    print("Bienvenido al generador de texto de OpenAI. Ingresa 'exit' para salir.")
    while True:
        # Se obtiene la entrada del usuario de manera segura
        prompt = get_input("Ingresa un prompt: ")
        if not prompt:
            continue
        # Se verifica si el usuario desea salir del programa
        if prompt.lower() in ['exit', 'salir', 'quit', 'terminar']:
            print("Saliendo del programa...")
            break
        # Se genera el texto a partir del prompt dado por el usuario
        print("Generando texto...")
        response = generate_text(prompt, engine_model_gpt3, temperature=0.5)
        if response is None:
            continue
        # Se muestra el texto generado en la pantalla
        print(response)

if __name__ == "__main__":
    main()
