"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
# pylint: disable=import-outside-toplevel

def pregunta_01():
    import os
    import matplotlib.pyplot as plt

    # Datos de los años y porcentaje de uso de cada medio
    años = list(range(2001, 2011))
    uso_tv = [74, 76, 75, 72, 70, 69, 70, 68, 68, 66]
    uso_periodico = [45, 43, 48, 46, 40, 35, 34, 34, 30, 31]
    uso_radio = [18, 20, 17, 18, 16, 15, 14, 13, 16, 16]
    uso_internet = [13, 14, 17, 20, 18, 20, 22, 22, 40, 41]

    plt.figure(figsize=(8, 6))

    # Graficar cada medio con su respectivo color y etiqueta
    plt.plot(años, uso_tv, label="Televisión", color="black")
    plt.plot(años, uso_periodico, label="Periódico", color="gray")
    plt.plot(años, uso_radio, label="Radio", color="lightgray")
    plt.plot(años, uso_internet, label="Internet", color="dodgerblue", marker="o")

    # Etiquetas al final de cada línea (año 2010)
    plt.text(2010, uso_tv[-1], f"{uso_tv[-1]}%", va="center", ha="left", color="black")
    plt.text(2010, uso_periodico[-1], f"{uso_periodico[-1]}%", va="center", ha="left", color="gray")
    plt.text(2010, uso_radio[-1], f"{uso_radio[-1]}%", va="center", ha="left", color="lightgray")
    plt.text(2010, uso_internet[-1], f"{uso_internet[-1]}%", va="center", ha="left", color="dodgerblue")

    # Etiquetas al inicio de cada línea (año 2001)
    plt.text(2001, uso_tv[0], f"Televisión {uso_tv[0]}%", va="center", ha="right", color="black")
    plt.text(2001, uso_periodico[0], f"Periódico {uso_periodico[0]}%", va="center", ha="right", color="gray")
    plt.text(2001, uso_radio[0], f"Radio {uso_radio[0]}%", va="center", ha="right", color="lightgray")
    plt.text(2001, uso_internet[0], f"Internet {uso_internet[0]}%", va="center", ha="right", color="dodgerblue")

    # Título principal y subtítulo
    plt.suptitle("Una proporción creciente cita Internet como su fuente principal de noticias",
             y=0.85, fontsize=10)
    plt.title("Cómo la gente obtiene sus noticias", fontsize=14, weight='bold')

    plt.xticks(años)
    plt.yticks([])

    plt.box(False)

    os.makedirs("files/plots", exist_ok=True)

    plt.savefig("files/plots/news.png", bbox_inches="tight")
    plt.close()

"""
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
"""
