# MSFP2
Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel
[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212228-hue/MSFP2)

# Práctica 2: Modelado y control del sistema cardiovascular mediante el modelo Windkessel

## Información de la estudiante
Mariant Reyes Zamudio [23212228] ; l23212228@tectijuana.edu.mx  
Modelado de Sistemas Fisiológicos  
Ingeniería Biomédica  

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx  
Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura
El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos
1. Formular el modelo dinámico en espacio de estados y la función de transferencia $G(s) = P_p(s)/P_a(s)$ del modelo Windkessel de cuatro elementos ($Z, C, R, L$).
2. Analizar analíticamente la estabilidad y el error en estado estacionario para las condiciones normotensa (control), hipotensa e hipertenso.
3. Emular la respuesta del sistema cardiovascular en Simulink mediante tres representaciones: ecuaciones de estado, función de transferencia y circuito equivalente en Simscape Electrical.
4. Generar una señal de excitación estocástica mediante el bloque *Uniform Random Number* ($T_s = 0.1\text{ s}$) para simular la respuesta en lazo abierto de los tres modelos en $t \in [0, 15]\text{ s}$.
5. Diseñar y sintonizar controladores PID en Simulink (*Tune*) para reducir las desviaciones del caso hipotenso y del caso hipertenso con respecto a la referencia normotensa.
6. Evaluar y comparar el comportamiento en lazo cerrado para los esquemas normotenso-hipotenso y normotenso-hipertenso.
7. Desarrollar y validar los modelos y simulaciones computacionales en MATLAB y Python (VS Code), realizando una verificación cruzada de resultados entre plataformas.
8. Elaborar un diagrama biológico en BioRender que vincule los elementos del modelo Windkessel con la anatomía y hemodinámica cardiovascular.

## Descripción detallada del sistema

El modelo Windkessel de cuatro elementos representa las propiedades hemodinámicas del sistema arterial combinando resistencia periférica, distensibilidad arterial, impedancia característica de la aorta proximal e inertancia de la masa sanguínea en movimiento. Mediante la analogía entre variables hemodinámicas y eléctricas ($\text{Presión} \to \text{Voltaje}$, $\text{Flujo sanguíneo} \to \text{Corriente}$), el circuito equivalente consta de:
* $Z$: Impedancia característica de la región proximal ($\text{mmHg}\cdot\text{s}/\text{ml}$).
* $L$: Inertancia arterial asociada con los efectos inerciales del flujo ($\text{mmHg}\cdot\text{s}^2/\text{ml}$).
* $R$: Resistencia periférica total que representa la oposición al flujo ($\text{mmHg}\cdot\text{s}/\text{ml}$).
* $C$: Distensibilidad arterial total que modela el almacenamiento de volumen ($\text{ml}/\text{mmHg}$).

Aunque cuenta con cuatro componentes, la presencia de dos elementos independientes de almacenamiento de energía ($C$ y $L$) define al sistema como un modelo de segundo orden descritible por las variables de estado $x(t) = [F_L(t) \quad P_p(t)]^T$, donde $F_L(t)$ es el flujo a través de la inertancia y $P_p(t)$ es la presión sobre la distensibilidad arterial.

Las diferencias hemodinámicas entre los pacientes se modelan variando únicamente la distensibilidad arterial ($C$), manteniendo constantes $Z = 0.010$, $L = 0.001$ y $R = 1.000$:

| Parámetro | Hipotenso | Normotenso (Control) | Hipertenso | Unidades |
| :--- | :---: | :---: | :---: | :---: |
| Impedancia proximal ($Z$) | $0.010$ | $0.010$ | $0.010$ | $\text{mmHg}\cdot\text{s}/\text{ml}$ |
| Inertancia arterial ($L$) | $0.001$ | $0.001$ | $0.001$ | $\text{mmHg}\cdot\text{s}^2/\text{ml}$ |
| Resistencia periférica ($R$) | $1.000$ | $1.000$ | $1.000$ | $\text{mmHg}\cdot\text{s}/\text{ml}$ |
| Distensibilidad arterial ($C$) | $3.500$ | $1.500$ | $1.000$ | $\text{ml}/\text{mmHg}$ |

Palabras clave: Circuito RLC; Control PID; Modelo Windkessel; Sistema cardiovascular; Hemodinámica; Simulaciones numéricas.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [`.mlx` y `.pdf`].
2. Modelo de Simulink y Simscape Electrical [`.slx`].
3. Código de verificación en Python / Visual Studio Code [`.py`].
4. Diagrama biológico del sistema cardiovascular [`.png` / `.pdf`].
5. Capturas y tablas con los parámetros de sintonización de los controladores PID.
6. Figuras comparativas de lazo abierto y lazo cerrado en MATLAB y Python [formatos `.pdf`].
7. Archivo de citación bibliográfica [`CITATION.cff`].

## Referencias
[1] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

[2] F. C. Hoppensteadt and C. S. Peskin, *Modeling and Simulation in Medicine and the Life Sciences*, 2nd ed. New York, USA: Springer, 2002.

[3] J. E. Hall, *Guyton and Hall Textbook of Medical Physiology*, 14th ed. Philadelphia, PA, USA: Elsevier, 2021.

[4] K. Ogata, *Ingeniería de Control Moderna*, 5a ed. Madrid, España: Pearson Educación, 2010.

[5] N. S. Nise, *Control Systems Engineering*, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

[6] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2026. Permalink: https://biomath.xyz/course/

[7] Tecnológico Nacional de México, *Programa de estudio de la asignatura Modelado de Sistemas Fisiológicos*, IBF-1020.
