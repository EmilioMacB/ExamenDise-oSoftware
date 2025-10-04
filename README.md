# Examen de Refactorización - Principios SOLID

**Autor:** Emilio Maciel
**Fecha:** 3 de Octubre de 2025

## Descripción del Proyecto

Este proyecto consiste en la refactorización de un sistema de biblioteca (`biblioteca_examen.py`) que no cumplia con los principios SOLID. 


## Resumen de Refactorizaciones


### Ejercicio 1: Open/Closed Principle (OCP)

* **Problema:** El método `buscar_libro()` usaba una cadena de `if/elif`, lo que lo hacía cerrado a la extensión. Agregar un nuevo criterio de búsqueda requería modificar su código.
* **Solución:** 
    1.  Se creó una interfaz abstracta `EstrategiaBusqueda`.
    2.  Se desarrollaron clases concretas para cada criterio de búsqueda (`BusquedaPorTitulo`, `BusquedaPorAutor`, etc.), cada una con su propia lógica.
    3.  El método `buscar_libro()` fue refactorizado para recibir un objeto de estrategia, delegándole la lógica de la comparación.
* **Resultado:** El sistema ahora está **abierto a la extensión**. Se pudo agregar una nueva `BusquedaPorDisponibilidad` sin modificar la clase `SistemaBiblioteca`.

### Ejercicio 2: Single Responsibility Principle (SRP)

* **Problema:** La clase `SistemaBiblioteca` era una clase que queria hacer de todo: validación de datos, lógica de negocio, persistencia y notificaciones.
* **Solución :** La clase fue descompuesta:
    1.  `ValidadorBiblioteca`: Encapsula todas las reglas de validación.
    2.  `RepositorioBiblioteca`: Maneja exclusivamente la persistencia de datos.
    3.  `ServicioNotificaciones`: Se encarga únicamente de enviar notificaciones.
* **Resultado:** La clase `SistemaBibliotecaSRP` ahora actúa como un **orquestador**, coordinando los componentes. Cada clase tiene una única razón para cambiar.

### Ejercicio 3: Dependency Inversion Principle (DIP)

* **Problema Identificado:** El módulo de alto nivel (`SistemaBibliotecaSRP`) dependía directamente de una implementación de bajo nivel (`RepositorioBiblioteca`).
* **Solución :** Se invirtió la dependencia mediante una abstracción.
    1.  Se creó la interfaz `IRepositorioBiblioteca`, que define un contrato para cualquier repositorio.
    2.  La clase `RepositorioArchivo` (y la extra, `RepositorioMemoria`) se modificaron para implementar esta interfaz.
    3.  La clase `SistemaBibliotecaDIP` fue refactorizada para depender de la interfaz `IRepositorioBiblioteca`, no de una clase concreta. La implementación específica se "inyecta" en el constructor.
* **Resultado:**  Podemos cambiar el mecanismo de persistencia (de archivos a memoria, o en el futuro a una base de datos) sin realizar ningún cambio en la lógica de negocio principal. esto lo hace un sistema muy flexible.