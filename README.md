# # :penguin: Clasificador de Pingüinos 
Este proyecto es una aplicación web desarrollada con Flask que permite predecir el sexo de un pingüino a partir de características físicas como la longitud y profundidad del pico, la longitud de la aleta y la masa corporal. El modelo de clasificación se ha entrenado utilizando AdaBoost con los datos balanceados mediante SMOTE, y ha sido guardado en un archivo `.pkl`

## :jigsaw: Modelo de cluster y :chart_with_upwards_trend: clasificación
[Colab](https://colab.research.google.com/drive/1nthSjExKFz8QvYPAK6YfNQqdNWHs_3gF)

### :package: Características del proyecto
 - Modelo ML de clasificasión entrenado con AdaBoost (`scikit-learn`)
 - Interfaz sencilla (`Bootstrap`)
 - Explicación de cada característica de entrada

### :inbox_tray: Variables Utilizadas como Valores de entrada

| Variable            | Descripción                        |
|:-------------------:|:----------------------------------:|
| `bill_length_mm`    | Longitud del pico en milímetros    |
| `bill_depth_mm`     | Profundidad del pico en milímetros | 
| `flipper_length_mm` | Longitud de la aleta en milímetros | 
| `body_mass_g`       | Masa corporal en gramos            |