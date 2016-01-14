# Notas

## Deploy Software Manually

* Un maravilloso jueves por la mañana, soleado. Aparece alguien por tu mesa y y
  te comenta eso de -Venga figura, que ya podemos sacar esto a producción - Nos
  aparece un fichero "deploy.txt" con documentación "detallada" y paso a paso.
  Naturalmente, para hacer a mano.

* Se confía en pasos manuales para confirmar que todo está funcionando bien.

* Hay que llamar a desarrollo, que estarán encantados de ayudarnos. Y nos
  preguntarán 50 veces si hemos leído el documento.

* Resulta que hay algunos pasos que se nos habían olvidado y hay que cambiarlos
  para que se adecue a las políticas de seguridad.

* Los entornos son diferentes! Diferentes sistemas de ficheros, diferentes
  layouts ...

* Nos cuesta bastante sacar una release.

* ¿O no sabemos cuanto nos cuesta?

* Acabas ese jueves a las 3 de la mañana, con un día que ya no es tan
  maravilloso como tu pensabas. Y todavía no llega a funcionar!


### En su lugar

Debería ser un proceso totalmente *automatizado*. Deberíamos tener 2 inputs:

* Qué version
* Qué entorno

Sabemos que:

* Si no están totalmente automatizados ocurren errores.
* Al ocurrir errores, aleatorios, no es un proceso confiable.
* Necesita una documentación, y un mantenimiento.
* Bus factor: ¿Qué pasa si le toca la lotería a nuestro "experto"?
* Al ser manual, es largo, tedioso. Si te aburres, aún hay más errores.


## Deploy to a Production-like environment after development is complete

* Esto es waterfallista!
* Los testers lo han probado sólo en desarrollo
* Operaciones es la primera vez que ven esta aplicación. Esto es un puto silo.
* Caro
* Las configuraciones que hay en desarrollo a veces no tienen nada que ver con
  lo que hay en producción
* No hay colaboración. Se mantiene la mentalidad de los silos.

### Analizando un poco más

* El primer deploy siempre es el más jodido. Primeros bugs, a veces hay prisas
* El tiempo de ciclo. Cuanto más largo, más cosas se suponen.
* Coordinar y comunicar silos no es fácil
* Diferencias de entornos: Se comporta igual el path en windows que en un
  freeBSD? -> Explica el caso de los slash + JVM

### En su lugar

Queremos que esto sea un proceso integrador. Todo el equipo debe ser responsable
del proceso de deploy. Si añades valor, pero no llega. No existe ese valor.

## Manual configuration management of production environments

* Ya hemos desplegado varias veces a staging, pero el paso a producción nos
  falla
* Diferentes miembros de un cluster. No es homogeneo, no se reparte la carga.
  Puedes hablar de escalado horizontal.
* A operaciones le cuesta un montón sacar una máquina.
* No puedes volver atrás en una versión

* Snowflake Servers: Cada servidor es único, como un bonito como de nieve.
* Se tocan las cosas directamente en producción.

### En su lugar

Sabemos que los sistemas de control de versiones funcionan, es la primera piedra
de la automatización.


## Feedback

Quereemos un proceso automatizado y frecuente.

Cada cambio debería tirar un proceso de realimentación.
Esa realimentación tiene que llegar rápido.
Se debe actuar sobre esa realimentación.

Creo que es Deiming quien habla de que cuanto antes se encuentra un error, más
barato es arreglarlo. Build quality in.
