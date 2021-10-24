# Heart Failure 💔 Machine Learning

Trabajo Práctico para la materia **Aprendizaje Automático** de UNSAM


## 📝 Introducción

A partir del dataset a trabajar (extraído de **Kaggle** [aquí](https://www.kaggle.com/andrewmvd/heart-failure-clinical-data)) realizaremos las primeras prácticas de prueba para conocer el dataset en una Jupyter Notebook.
Luego de explorar los datos, seguiremos con la predicción y elección de un modelo.

[Paper original](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0181001)


## 📦 Dependencias y ejecución
Para poder trabajar localmente, se debe hacer lo siguiente **(líneas que empiezan con #, son el alternativo de la línea anterior para usuarios en Linux)**:
1. Clonar el repositorio
```
cd ./carpeta/en/donde/clonar/repo
git clone https://github.com/JaviCeRodriguez/Heart-Failure-ML.git
```

2. Crear un entorno virtual y activarlo
```
cd ./Heart-Failure-ML

python -m venv myvenv
# python3 -m venv my-project-env

myvenv/Scripts/activate
# source myvenv/bin/activate
```

3. Instalar librerías
```
pip install -r requirements.txt
```
Opcionalmente, pueden utilizar el entorno virtual creado por Anaconda!

4. Para desactivar el entorno (si necesario)
```
deactivate
```

Estaremos trabajando en la notebook `main.ipynb`, pero daremos su versión en formato `*.py`. Podemos ejecutar la notebook
en Jupyter Notebook, Google Colab o desde Visual Studio Code. Recomendamos utilizar PyCharm, ya que facilita la instalación
de las librerías en el entorno virtual y de la extensión Jupyter Notebook.


## 📋 Dataset

Como mencionamos anteriormente, el dataset utilizado trata sobre datos recolectados (299 muestras) a partir de pacientes con falla cardíaca. Contiene las siguientes features: `age`, `anaemia`, `creatinine_phosphokinase`, `diabetes`, `ejection_fraction`, `high_blood_pressure`, `platelets`, `serum_creatinine`, `serum_sodium`, `sex`, `smoking`, `time` y `DEATH_EVENT`.


## 👩‍🎓👨‍🎓 Integrantes del grupo

<table align="center">
    <tr>
        <th>
            Javier Rodriguez
        </th>
        <th>
            Martin Pierangeli
        </th>
        <th>
            Marcelo Raponi
        </th>
        <th>
            Maria Luz Perez Saura
        </th>
    </tr>
    <tr>
        <td align="center">
        <a href="https://github.com/JaviCeRodriguez">
            <img src="https://avatars.githubusercontent.com/u/68615684?v=4" width=110 height=110 />
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/mpierangeli">
            <img src="https://avatars.githubusercontent.com/u/75583581?v=4" width=110 height=110 />
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/mraponi74">
            <img src="https://avatars.githubusercontent.com/u/88469172?v=4" width=110 height=110 />
        </a>
        </td>
        <td align="center">
        <a href="https://github.com/Luzperezsaura">
            <img src="https://avatars.githubusercontent.com/u/87423696?v=4" width=110 height=110 />
        </a>
        </td>
    </tr>
</table>