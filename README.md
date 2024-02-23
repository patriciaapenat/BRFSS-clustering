[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) 
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)

# Proyecto de Clustering con BRFSS

Este proyecto se centra en el análisis de clustering de los datos de la Encuesta de Factores de Riesgo de Comportamiento (BRFSS, por sus siglas en inglés) utilizando PySpark y TensorFlow. A través de una serie de notebooks Jupyter, se realiza una exploración detallada y un procesamiento de los datos de salud pública para identificar patrones y agrupaciones significativas en el comportamiento y las condiciones de salud de los encuestados.

## Estructura del Proyecto
El proyecto está dividido en cinco notebooks principales, cada uno enfocado en una etapa específica del proceso de análisis:

1. **Transformación Inicial**: Conversión de datos desde formato `.xpt` a `.csv`, facilitando su manipulación con PySpark.
2. **Filtrado Inicial**: Limpieza y selección de las variables relevantes para el estudio a partir de la documentación oficial de la BRFSS.
3. **Imputación de Valores Nulos**: Técnicas de imputación aplicadas para manejar los valores ausentes en el conjunto de datos.
4. **Análisis Exploratorio**: Visualización y exploración de los datos para obtener insights preliminares sobre las características demográficas y de salud de los encuestados.
5. **Aplicación de Algoritmos de Clustering**: Uso de autoencoders para reducción de dimensionalidad seguido por el algoritmo K-Means para identificar clusters en los datos.

## Resultados
Los análisis realizados revelaron varios patrones y clusters significativos entre los encuestados, destacando diferencias en los comportamientos de salud y riesgo según variables demográficas y de salud. Los resultados del proyecto pueden ser útiles para informar políticas de salud pública y programas de intervención dirigidos.

## Tecnologías Utilizadas

<p align="left">
  <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="40" height="40"/>
  </a>
  <a href="https://www.python.org" target="_blank" rel="noreferrer">
    <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
  </a>
  <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="40" height="40"/>
  </a>
  <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer">
    <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="40" height="40"/>
  </a>
  <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer">
    <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="40" height="40"/>
  </a>
  <a href="https://spark.apache.org/docs/latest/api/python/index.html" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Apache_Spark_logo.svg/512px-Apache_Spark_logo.svg.png" alt="Spark" width="40" height="40"/>
  </a>
  <a href="https://hadoop.apache.org/" target="_blank" rel="noreferrer">
    <img src="https://cdn.worldvectorlogo.com/logos/hadoop.svg" alt="Hadoop" width="74" height="40"/>
  </a>
</p>
