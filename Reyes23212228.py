"""
Práctica 2: Modelado y control del sistema cardiovascular mediante
el modelo Windkessel

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Mariant Reyes Zamudio
Número de control: 23212228
Correo institucional: l23212228@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy import signal
import control as ctrl
import pandas as pd

# Datos de la simulación
u = pd.read_excel('signal.xlsx', header=None).values.flatten()
x0, t0, tend, dt, w, h = 0, 0, 15, 1E-3, 10, 5
N = round((tend - t0) / dt) + 1 
t = np.linspace(t0, tend, N) 
u = signal.resample(u, len(t))

# Componentes del circuito RLC y modelo cardiovascular
def cardio(Z, R, L, C):
    num = [L * R, R * Z]
    den = [C * L * R * Z, L * (Z + R), R * Z]
    sys = ctrl.tf(num, den)
    L_poles = np.roots(den)
    return sys, L_poles

# Funcion de transferencia hipotenso
Z, R, L, C = 0.010, 1.000, 0.001, 3.500
syshipo, Lhipo = cardio(Z, R, L, C)
print(f"Función de transferencia para sistema hipotenso: {syshipo}")
print(f"Polos del sistema: L1 = {Lhipo[0]:.3e}, L2 = {Lhipo[1]:.3e}\n")

# Funcion de transferencia normotenso
Z, R, L, C = 0.010, 1.000, 0.001, 1.500
sysnormo, Lnorm = cardio(Z, R, L, C)
print(f"Función de transferencia para sistema normotenso (control): {sysnormo}")
print(f"Polos del sistema: L1 = {Lnorm[0]:.3e}, L2 = {Lnorm[1]:.3e}\n")

# Funcion de transferencia hipertenso
Z, R, L, C = 0.010, 1.000, 0.001, 1.000
syshiper, Lhiper = cardio(Z, R, L, C)
print(f"Función de transferencia para sistema hipertenso (control): {syshiper}")
print(f"Polos del sistema: L1 = {Lhiper[0]:.3e}, L2 = {Lhiper[1]:.3e}\n")

# Respuesta del sistema en lazo abierto
_, PpN = ctrl.forced_response(sysnormo, t, u, x0)
_, PpL = ctrl.forced_response(syshipo, t, PpN, x0)
_, PpH = ctrl.forced_response(syshiper, t, PpN, x0)

# Colores
clr1 = np.array([66, 133, 244]) / 255   # Azul
clr2 = np.array([234, 67, 53]) / 255   # Rojo
clr3 = np.array([251, 188, 5]) / 255   # Amarillo

# Controlador PID analógico
def controlador(kI, kP, kD, sys):
    Cr = 1E-6
    Re = 1 / (Cr * kI)
    Rr = kP * Re
    Ce = kD / Rr
    numPID = [Re * Rr * Ce * Cr, (Re * Ce + Rr * Cr), 1]
    denPID = [Re * Cr, 0]
    PID = ctrl.tf(numPID, denPID)
    sysPID = ctrl.feedback(ctrl.series(PID, sys), 1, sign=-1)
    return sysPID

# Argumentos ordenados exactamente como la definición: (kI, kP, kD, sys)
hipoPID = controlador(11182.6731, 45.9868, 0.0058, syshipo)
print(f"Función de transferencia del sistema hipotenso en lazo cerrado: {hipoPID}\n") 

hiperPID = controlador(2969.6366, 10.4054, 0.0018, syshiper)
print(f"Función de transferencia del sistema hipertenso en lazo cerrado: {hiperPID}\n")

_, PID1 = ctrl.forced_response(hipoPID, t, PpN, x0)
_, PID2 = ctrl.forced_response(hiperPID, t, PpN, x0)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']

#plot individuos
fg1 = plt.figure(1)
fg1.set_size_inches(w, h)
plt.plot(t, PpL, '-', linewidth=0.5, color=clr2, label='Pp(t): Hipotenso')
plt.plot(t, PpH, '--', linewidth=0.5, color=clr3, label='Pp(t): Hipertenso')
plt.plot(t, PpN, ':', linewidth=0.5, color=clr1, label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0, 15]); plt.xticks(np.arange(0, 15.1, 1))
plt.ylim([-0.4, 1.6]); plt.yticks(np.arange(-0.4, 1.6, 0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3, frameon=True)
fg1.tight_layout()
fg1.savefig('individuos_python.pdf', bbox_inches='tight')
plt.show()

#plot hipotenso
fg2 = plt.figure(2)
fg2.set_size_inches(w, h)
plt.plot(t, PpL, '-', linewidth=0.5, color=clr2, label='Pp(t): Hipotenso')
plt.plot(t, PID1, '--', linewidth=0.5, color=clr3, label='PID(t): Hipotenso')
plt.plot(t, PpN, ':', linewidth=0.5, color=clr1, label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0, 15]); plt.xticks(np.arange(0, 15.1, 1))
plt.ylim([-0.4, 1.6]); plt.yticks(np.arange(-0.4, 1.6, 0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3, frameon=True)
fg2.tight_layout()
fg2.savefig('Hipotenso_python.pdf', bbox_inches='tight')
plt.show()

# Plot hipertenso
fg3 = plt.figure(3)
fg3.set_size_inches(w, h)
plt.plot(t, PpH, '-', linewidth=0.5, color=clr2, label='Pp(t): Hipertenso')
plt.plot(t, PID2, '--', linewidth=0.5, color=clr3, label='PID(t): Hipertenso')
plt.plot(t, PpN, ':', linewidth=0.5, color=clr1, label='Pp(t): Normotenso')
plt.grid(False)
plt.xlim([0, 15]); plt.xticks(np.arange(0, 15.1, 1))
plt.ylim([-0.4, 1.6]); plt.yticks(np.arange(-0.4, 1.6, 0.2))
plt.xlabel('t [s]')
plt.ylabel('Pp(t) [V]')
plt.legend(bbox_to_anchor=(0.5, -0.25), loc='center', ncol=3, frameon=True)
fg3.tight_layout()
fg3.savefig('Hipertenso_python.pdf', bbox_inches='tight')
plt.show()