# ¿Qué expresiones utiliza este programa?

Veamos a continuación que expresiones serán útiles para la confección de este programa:

En primer lugar a partir de la masa se calcula el __Peso__ del cuerpo:

$$ P=m.g$$

A partir de la descomposición en los dos ejes podemos calcular las componentes P<sub>x</sub> y P<sub>y</sub>:

$$P_x=P.cos \theta $$

$$P_y=P.sen \theta $$

Salvo que se especifique en la letra del ejercicio supondremos que no actúan fuerzas extras en el eje y, por lo tanto
la fuerza Normal será igual y opuesta a la componente P<sub>y</sub>:

$$N=P_y $$

La fricción depende del coeficiente de rozamiento y la Normal:

$$F_r= \mu . N $$

La condición para que el cuerpo esté en equilibrio es que la componente P<sub>x</sub> sea igual o menor que el rozamiento máximo:

$$ P_x \leq F_r  \Leftrightarrow a=0$$

Si la componente P<sub>x</sub> es mayor al rozamiento se puede despejar la aceleración a partir de la Fuerza neta y utilizando la segunda ley de Newton:

$$F_Neta=m.a$$

$$P_x - F_r = m.a$$

$$a=\frac{P_x - F_r}{m}$$

Si trabajáramos de forma paramétrica (sin datos) podemos expresar la última ecuación de una forma más elegante:

$$a=\frac{m.g.sen \theta - \mu m.g.cos \theta}{m}$$

$$a=g(sen \theta - \mu.cos \theta)$$

Vemos que la aceleración del objeto no depende de su masa y solo depende del valor de g, mu y el ángulo del plano.
