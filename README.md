# Laboratorio-1-experimentos-con-problemas-de-optimizaci-n
Laboratorio I Optimización 

## Punto 1
#### Problema de Optimización: Minimización del Costo de Producción

#### Descripción

Una empresa produce dos tipos de productos, \( P_1 \) y \( P_2 \), que requieren recursos limitados. El objetivo es minimizar el costo total de producción sujeto a restricciones de recursos.

#### Función objetivo:
El costo total de producción es la suma de los costos de producir \( P_1 \) y \( P_2 \):
\[
C(x, y) = 5x^2 + 8y^2
\]
donde:
- \( x \): cantidad producida de \( P_1 \)
- \( y \): cantidad producida de \( P_2 \)

El objetivo es minimizar \( C(x, y) \).

#### Restricciones:
La producción de \( P_1 \) y \( P_2 \) está limitada por los siguientes recursos:

1. **Recurso A**: se limita a 40 unidades. Cada unidad de \( P_1 \) consume 2 unidades de A, y cada unidad de \( P_2 \) consume 3 unidades de A.
   \[
   2x + 3y \leq 40
   \]

2. **Recurso B**: se limita a 36 unidades. Cada unidad de \( P_1 \) consume 4 unidades de B, y cada unidad de \( P_2 \) consume 2 unidades de B.
   \[
   4x + 2y \leq 36
   \]

#### Objetivo:
Encontrar los valores óptimos de \( x \) y \( y \) que minimicen el costo total \( C(x, y) \) respetando las restricciones de los recursos.

#### Gráfica de la Región Factible

La región factible para este problema es la intersección de las restricciones. El gráfico muestra dicha región sombreada.

## Punto 2
### Series de Taylor
#### Descripción
Este proyecto proporciona una interfaz gráfica de usuario (GUI) para graficar expansiones en series de Taylor de funciones matemáticas comunes. La GUI está construida usando `tkinter`, y los cálculos matemáticos se realizan utilizando `sympy` y `numpy`. Los gráficos resultantes se muestran utilizando `matplotlib`.

#### Características
- Selección de una lista de funciones comunes: `sin(x)`, `cos(x)`, `exp(x)`, `log(1 + x)`, y `1 / (1 - x)`.
- Entrada del punto de expansión (`a`) y el número de términos (`n`) para la serie de Taylor.
- Graficar la expansión en serie de Taylor junto con la función original.

#### Cómo Usar
1. Ejecuta el script.
2. Selecciona la función que deseas expandir desde el menú desplegable.
3. Ingresa el punto de expansión (`a`) y el número de términos (`n`).
4. Haz clic en el botón "Graficar" para generar y mostrar el gráfico.

#### Dependencias
- `numpy`
- `matplotlib`
- `sympy`
- `tkinter`

## Punto 3
### Convertidor de Formato COO
#### Descripción
- Este proyecto proporciona una interfaz gráfica de usuario (GUI) para convertir una matriz densa en formato de almacenamiento por coordenadas (COO). La GUI está construida usando tkinter, y los cálculos se realizan utilizando numpy y scipy.sparse.

#### Características
- Entrada de una matriz densa de 4x4.
- Conversión de la matriz densa al formato COO.
- Visualización de los valores no nulos (NZ), índices de fila (IF) e índices de columna (IC) de la matriz en formato COO.
- Visualización de la matriz en formato COO.

##### Cómo Usar
- Ejecuta el script.
- Ingresa los valores de la matriz en los campos de entrada correspondientes.
- Haz clic en el botón "Convertir a COO" para realizar la conversión.
- Los resultados se mostrarán en la parte inferior de la ventana.
#### Dependencias
'numpy'
'scipy'
'tkinter'


#### Conclusión
- Este proyecto demuestra cómo utilizar varias bibliotecas de Python para crear una herramienta interactiva que facilita la conversión de matrices densas al formato COO. El uso de tkinter para la GUI, numpy para el manejo de matrices, y scipy.sparse para la conversión al formato COO, hace que esta aplicación sea útil y educativa.
## Conclusiones Punto 4
### Gradient Descent

**Learning Rate (LR):**
- Un LR bajo requiere más iteraciones para converger, pero es más seguro y estable.
- Un LR alto (como 0.5) puede acelerar la convergencia, alcanzando el mínimo en pocas iteraciones.
- Sin embargo, un LR demasiado alto puede causar inestabilidad y hacer que el algoritmo no converja.

**Punto Inicial:**
- Iniciar desde un valor más cercano al mínimo (𝑥=2) reduce la cantidad de iteraciones necesarias para alcanzar el valor óptimo.
- Un punto inicial más lejano (como 𝑥=0) implica que el algoritmo tendrá que trabajar más para alcanzar el valor óptimo, aumentando el número de iteraciones.

**Número de Iteraciones:**
- Con un número bajo de iteraciones, el algoritmo no logra llegar al mínimo, especialmente si el LR es bajo.
- Aumentando el número de iteraciones, el algoritmo se sigue acercando al mínimo.
- Con tasas de aprendizaje más altas, el número de iteraciones necesarias se reduce considerablemente, pero se debe tener cuidado con la estabilidad.

### Newton´s Method 
**Efecto del valor inicial (x0):**
- Un valor inicial más cercano a la raíz, como x0 = 0.5, permite una convergencia rápida (1 iteración).
- Valores iniciales más alejados de la raíz, como x0 = 0.1, requieren más iteraciones para alcanzar la convergencia (5 o más iteraciones).

**Cantidad de iteraciones (max_iter):**
- Con pocas iteraciones (3), es posible que no se alcance la convergencia completa (f(x) ≈ 1.70902).
- Aumentar las iteraciones (de 5 a 8) no cambia el resultado si el método ya ha convergido (f(x) ≈ 1.69315).

**Velocidad de convergencia:**
- La velocidad de convergencia depende mucho del valor inicial. Un valor inicial adecuado puede hacer que el método converja en pocas iteraciones.

### Genetic Algorithm

**Número de Generaciones:**
- Conclusión: Más generaciones mejoran los resultados.
- Pocas generaciones (Exp 1, 2 generaciones): Resultó en una solución peor (f(x) = 1.82993).
- Suficientes generaciones (Exp 2, 30 generaciones): Mejoró significativamente (f(x) = 1.69315).

**Tamaño de la Población:**
- Conclusión: Un tamaño de población moderado (10) es suficiente.
- Poblaciones pequeñas (Exp 4, 5 individuos): Afectan negativamente la solución (f(x) = 1.69484).
- Poblaciones grandes (Exp 3, 40 individuos): No mejoran mucho el resultado en este caso.

**Tasa de Mutación:**
- Conclusión: Una tasa moderada (0.1) funciona mejor.
- Alta tasa de mutación (Exp 5, 0.5): Introduce demasiado ruido (f(x) = 1.69371).
- Baja tasa de mutación (Exp 6, 0.01): Limita la exploración (f(x) = 1.69963).

**Puntos Clave:**
- Generaciones: Más de 10 son recomendables.
- Población: Un tamaño de 10 es equilibrado.
- Mutación: La tasa óptima en este caso es alrededor de 0.1.