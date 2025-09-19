# Análisis de Señales en Python

## Propósito
Este proyecto tiene como objetivo ilustrar la representación en el dominio del tiempo y la frecuencia de distintas señales usando Python. Permite visualizar señales comunes como el 
pulso rectangular, el escalón unitario y una señal senoidal, junto con sus espectros de magnitud y fase mediante la Transformada Discreta de Fourier (FFT).

## Descripción del Código
El código realiza lo siguiente:

1. **Parámetros de muestreo**:  
   - `Fs`: Frecuencia de muestreo (1000 Hz)  
   - `T`: Periodo de muestreo  
   - `N`: Número de puntos para la señal  
   - `t`: Vector de tiempo desde -1 a 1 segundo

2. **Señales generadas**:  
   - `rect`: Pulso rectangular de ancho 0.4 s  
   - `u`: Escalón unitario  
   - `seno`: Señal senoidal de 5 Hz

3. **Función `plot_fft(signal, title)`**:  
   - Calcula la FFT de la señal  
   - Calcula las frecuencias asociadas  
   - Grafica la señal en tres subgráficas:
     1. Señal en el dominio del tiempo  
     2. Magnitud del espectro  
     3. Fase del espectro

4. **Ejecución**:  
   Llama a `plot_fft` para cada señal y genera las gráficas correspondientes.

## Requisitos
- Python 3.x  
- Librerías:
  ```bash
  pip install numpy matplotlib
