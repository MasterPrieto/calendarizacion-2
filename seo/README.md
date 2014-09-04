# SEO: Servidor de Optimizacion (metaheur&iacute;stico)

Es la implementacion de un servidor gen&eacute;rico de optimizaci&oacute;n basado en metaheur&iacute;sticas.

La idea es que este servidor le sirva a un sistema de calendarizaci&oacute;n de maestros/horarios/cursos para generar las programaciones de horarios.

Se va a utilizar un enfoque de iniciativa mixta, por lo cual el proceso de calendarizaci&oacute;n ser&aacute; "interactivo" y el usuario podr&aacute; definir nuevas restricciones o cambiar los bounds del problema para fijar instancias en ciertas horas o espacios.

Debe poder recibir todo lo necesario para realizar una b&uacute;squeda usando metaheur&iacute;sticas. Con estos datos se van a construir las funciones de evaluaci&oacute;n y factibilidad, las cuales se utilizan para darle costo o _fitness_ a una soluci&oacute;n, la cual puede ser factible o infactible seg&uacute;n las restricciones duras enviadas.

La funci&oacute;n de evaluaci&oacute;n se va a construir a partir de las restricciones blandas.

## Usage

FIXME

## Test

Durante el desarrollo se puede utilizar _lein autoexpect_ para estar corriendo los tests cada vez que cambian. Es preferible tener una ventana abierta para ello.

$ lein autoexpect

o se puede utilizar _lein expectations_ para checar los tests una sola vez y ya.

## License

Copyright © 2014 FIXME

Distributed under the Eclipse Public License either version 1.0 or (at
your option) any later version.
