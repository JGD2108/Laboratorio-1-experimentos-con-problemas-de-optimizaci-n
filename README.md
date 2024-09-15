# Laboratorio-1-experimentos-con-problemas-de-optimizaci-n
Laboratorio I Optimización 

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