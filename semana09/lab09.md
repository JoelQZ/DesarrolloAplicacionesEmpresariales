# Informe de Laboratorio N° 09 - Introducción a React y SPA con Vite

## Datos del Estudiante
- **Curso:** Desarrollo de Aplicaciones Empresariales (4 - C24 - Sección CD)
- **Tema:** Introducción a React: SPA, Node.js, npm, Vite, JSX, Listas y Renderizado Condicional
- **Proyecto:** Pizzería (Front-end en carpeta `frontend/`)

---

## PARTE 1 — Una interfaz React para la aplicación de las Semanas 4 a 8

### Ejercicio 1 — Verificar el entorno: Node.js y npm

**Respuesta:**
Se verificó la instalación previa de Node.js y npm en la terminal del sistema.

- Comandos ejecutados:
  ```powershell
  node -v
  npm -v
  ```

#### Tabla de Equivalencias de Tecnologías:
| Elemento | Entorno Python / Django | Entorno Node.js / React |
| :--- | :--- | :--- |
| **Lenguaje** | Python | JavaScript / JSX |
| **Gestor de Paquetes** | `pip` | `npm` |
| **Archivo de Dependencias** | `requirements.txt` | `package.json` |
| **Carpeta de Dependencias** | `venv/` (Entorno virtual) | `node_modules/` |
| **Comando del Servidor Dev** | `python manage.py runserver` | `npm run dev` |

*(Adjuntar captura de pantalla de la terminal mostrando la ejecución de `node -v` y `npm -v`)*

---

### Ejercicio 2 — Crear y ejecutar el proyecto con Vite

**Respuesta:**
Dentro de la raíz del repositorio de Django, se creó el proyecto de React bajo la carpeta `frontend/` utilizando Vite con la plantilla de JavaScript.

- Comandos ejecutados:
  ```powershell
  npm create vite@latest frontend -- --template react
  cd frontend
  npm install
  npm run dev
  ```

El servidor de desarrollo quedó levantado en `http://localhost:5173/`.

*(Adjuntar captura de pantalla de la terminal con `npm run dev` y del navegador en `http://localhost:5173/` mostrando la plantilla inicial de Vite)*

---

### Ejercicio 3 — Reconocer la estructura del proyecto

**Explicación con palabras propias:**
- **`index.html`**: Es el único archivo HTML de la aplicación (Single Page Application). Contiene un `<div id="root"></div>` donde React inyecta todo el contenido dinámico. *(Equivalente en Django: El maquetado `base.html` principal)*.
- **`main.jsx`**: Punto de entrada de JavaScript que toma el componente raíz `<App />` y lo monta dentro del contenedor `root` del HTML. *(Equivalente en Django: El archivo `wsgi.py` / `asgi.py` o la configuración inicial en `urls.py`)*.
- **`App.jsx`**: Es el componente principal de React donde se define la interfaz de usuario con JSX. *(Equivalente en Django: Una plantilla principal `index.html` o la vista raíz)*.
- **`package.json`**: Registra los metadatos del proyecto, scripts (`dev`, `build`, `lint`) y librerías instaladas. *(Equivalente en Django: `requirements.txt`)*.
- **`node_modules/`**: Carpeta donde se descargan e instalan todos los paquetes y dependencias físicas de Node.js. *(Equivalente en Django: La carpeta `venv/Lib/site-packages/`)*.

*(Adjuntar captura del árbol de archivos de la carpeta `frontend/` en VS Code)*

---

### Ejercicio 4 — Escribir el primer JSX con expresiones

**Respuesta:**
Se limpiaron los archivos de estilos (`App.css` e `index.css`) y se editó `App.jsx` para mostrar expresiones con llaves `{}`.

**Código de `src/App.jsx`:**
```jsx
function App() {
  const nombreApp = "Pizzería Gran Sabor - Menú Base";
  const precioBase = 25.0;
  const IGV = 0.18;

  const calcularPrecioTotal = (precio) => {
    return (precio * (1 + IGV)).toFixed(2);
  };

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>{nombreApp}</h1>
      <p>Precio base de Pizza Familiar: S/ {precioBase.toFixed(2)}</p>
      <p>Precio final con IGV (18%): S/ {calcularPrecioTotal(precioBase)}</p>
    </div>
  );
}

export default App;
```

*(Adjuntar captura del código en VS Code y del navegador mostrando el título y los cálculos)*

---

### Ejercicio 5 — Mostrar una lista con map() y key

**Respuesta:**
Se definió un arreglo de objetos simulando la respuesta JSON del endpoint de pizzas (`/api/pizzas/`) de la Semana 8. Se transformaron los decimales de cadena a números usando `Number().toFixed(2)`.

**Código agregado a `App.jsx`:**
```jsx
const pizzas = [
  { id: 1, nombre: "Pizza Pepperoni", precio_base: "28.50", disponible: true },
  { id: 2, nombre: "Pizza Hawaiana", precio_base: "26.00", disponible: true },
  { id: 3, nombre: "Pizza Suprema", precio_base: "32.00", disponible: false },
  { id: 4, nombre: "Pizza Vegetariana", precio_base: "24.00", disponible: true },
  { id: 5, nombre: "Pizza Cuatro Quesos", precio_base: "30.50", disponible: false },
];

// DENTRO DEL JSX:
<h2>Catálogo de Pizzas</h2>
<ul>
  {pizzas.map((pizza) => (
    <li key={pizza.id}>
      <strong>{pizza.nombre}</strong> - Precio: S/ {Number(pizza.precio_base).toFixed(2)}
    </li>
  ))}
</ul>
```

**Justificación técnica:**
El método `.map()` de JavaScript en React equivale al bucle `{% for pizza in pizzas %}` ... `{% endfor %}` de las plantillas de Django. En React es obligatorio agregar el atributo `key={pizza.id}` para que el DOM virtual identifique de forma única cada elemento de la lista y optimice el renderizado.

*(Adjuntar captura del navegador mostrando la lista generada)*

---

### Ejercicio 6 — Aplicar renderizado condicional

**Respuesta:**
Se incluyeron mensajes condicionales utilizando un operador ternario (`condicion ? a : b`), el operador lógico `&&`, y un mensaje de estado vacío.

**Código de prueba:**
```jsx
<h2>Catálogo de Pizzas (Con Renderizado Condicional)</h2>
{pizzas.length === 0 ? (
  <p>No hay registros de pizzas disponibles.</p>
) : (
  <ul>
    {pizzas.map((pizza) => (
      <li key={pizza.id}>
        <strong>{pizza.nombre}</strong> - S/ {Number(pizza.precio_base).toFixed(2)}{" "}
        {pizza.disponible ? (
          <span style={{ color: 'green' }}>(Disponible)</span>
        ) : (
          <span style={{ color: 'red' }}>(Agotado)</span>
        )}
        {!pizza.disponible && <em style={{ marginLeft: '10px', color: 'orange' }}>¡Agotado temporalmente!</em>}
      </li>
    ))}
  </ul>
)}
```

*(Adjuntar 2 capturas: 1. Lista normal con los estados Disponibles/Agotado; 2. Salida con `pizzas = []` mostrando "No hay registros de pizzas disponibles.")*

---

### Ejercicio 7 — Mostrar una relación 1:N con listas anidadas

**Respuesta:**
Se representó la relación 1:N entre `Pedidos` y sus `Detalles` (pizzas solicitadas), calculando el total a pagar mediante JavaScript.

**Código de `App.jsx`:**
```jsx
const pedidos = [
  {
    id: 101,
    cliente: "Carlos Pérez",
    detalles: [
      { id: 1, pizza: "Pepperoni", cantidad: 2, subtotal: 57.0 },
      { id: 2, pizza: "Inka Kola 1.5L", cantidad: 1, subtotal: 10.0 }
    ]
  },
  {
    id: 102,
    cliente: "Ana Gómez",
    detalles: [
      { id: 3, pizza: "Suprema", cantidad: 1, subtotal: 32.0 }
    ]
  }
];

// DENTRO DEL JSX:
<h2>Registro de Pedidos (Relación 1:N)</h2>
{pedidos.map((pedido) => {
  const totalPedido = pedido.detalles.reduce((acc, item) => acc + item.subtotal, 0);
  return (
    <div key={pedido.id} style={{ border: '1px solid #ccc', margin: '10px 0', padding: '10px' }}>
      <h3>Pedido #{pedido.id} - Cliente: {pedido.cliente}</h3>
      <ul>
        {pedido.detalles.map((det) => (
          <li key={det.id}>
            {det.cantidad}x {det.pizza} - Subtotal: S/ {det.subtotal.toFixed(2)}
          </li>
        ))}
      </ul>
      <p><strong>Total del Pedido: S/ {totalPedido.toFixed(2)}</strong></p>
    </div>
  );
})}
```

*(Adjuntar captura del navegador mostrando las tarjetas de pedidos con sus listas anidadas y totales calculados)*

---

### Ejercicio 8 — Agregar estilos y verificar el flujo completo

**Respuesta:**
Se aplicaron estilos mediante `className` con un archivo `App.css` y estilos en línea con `style={{ }}`. Se ejecutaron las herramientas de calidad y compilación.

- Comandos ejecutados:
  ```powershell
  npm run lint
  npm run build
  ```

**Diferencia entre esta interfaz y los Templates de la Semana 6:**
Los templates de Django procesaban las etiquetas en el servidor (*Server-Side Rendering*) y devolvían HTML estático terminado al navegador. En cambio, esta interfaz de React se ejecuta completamente en el cliente (*Single Page Application*), donde el navegador recibe JavaScript y construye el HTML dinámicamente en vivo sin necesidad de recargar la página.

**¿Qué falta para conectarla con la API de la Semana 8?**
Falta realizar las peticiones HTTP asíncronas (`fetch` o `axios`) dentro de hooks como `useEffect` para reemplazar los arreglos estáticos con datos consumidos en tiempo real desde los endpoints REST (`/api/pizzas/`, `/api/ingredientes/`).

*(Adjuntar captura de la terminal con la salida exitosa de `npm run lint` y `npm run build`)*

---

## PARTE 2 — Una interfaz React para la investigación propia (Pizzería)

### Ejercicio 9 — Identificar los datos de la investigación propia

#### Tabla de Equivalencias de la Investigación Propia:
| Concepto | Selección de la Investigación Propia |
| :--- | :--- |
| **Entidad Principal 1** | `Ingrediente` (Campos: id, nombre, stock, unidad_medida) |
| **Entidad Principal 2** | `Repartidor` (Campos: id, nombre, telefono, activo) |
| **Dato que activa mensaje condicional** | Campo `stock` en `Ingrediente` (`stock === 0` muestra "Agotado", `stock < 20` muestra "¡Últimas unidades!") |
| **Relación 1:N o Modelo Intermedio** | `Cliente` con sus `DatosEntrega` (OneToOne/1:N) o `Pizza` con `RecetaPizza` |
| **Modelo de API de la Semana 8 usado** | Estructura JSON de `/api/ingredientes/` y `/api/repartidores/` |

---

### Ejercicio 10 — JSX y listas de la investigación propia

**Respuesta:**
Se construyó el componente con los datos estáticos de las entidades `Ingrediente` y `Repartidor`.

**Código de `App.jsx`:**
```jsx
const ingredientes = [
  { id: 1, nombre: "Queso Mozzarella", unidad_medida: "gr", stock: 1500 },
  { id: 2, nombre: "Salsa de Tomate", unidad_medida: "ml", stock: 15 },
  { id: 3, nombre: "Pepperoni", unidad_medida: "gr", stock: 0 },
  { id: 4, nombre: "Masa Tradicional", unidad_medida: "unid", stock: 50 },
  { id: 5, nombre: "Aceitunas Negras", unidad_medida: "gr", stock: 8 }
];

const repartidores = [
  { id: 1, nombre: "Juan Pérez", telefono: "987654321", activo: true },
  { id: 2, nombre: "Maria López", telefono: "912345678", activo: false },
  { id: 3, nombre: "Carlos Ruiz", telefono: "955555555", activo: true }
];
```

*(Adjuntar captura del navegador con la renderización de las listas de ingredientes y repartidores)*

---

### Ejercicio 11 — Renderizado condicional y estilos en la investigación propia

**Respuesta:**
Se añadieron reglas de renderizado condicional con ternarios y `&&` para el stock de ingredientes y la disponibilidad de repartidores. Se aplicaron estilos CSS.

**Código JSX con Renderizado Condicional:**
```jsx
<section className="seccion-inventario">
  <h2>Control de Stock de Ingredientes</h2>
  {ingredientes.length === 0 ? (
    <p>No hay ingredientes registrados en la base de datos.</p>
  ) : (
    <ul className="lista-ingredientes">
      {ingredientes.map((item) => (
        <li key={item.id} className="item-ingrediente">
          <span style={{ fontWeight: 'bold' }}>{item.nombre}:</span> {item.stock} {item.unidad_medida}{" "}
          {item.stock === 0 ? (
            <span className="badge-agotado">AGOTADO</span>
          ) : (
            <span className="badge-disponible">EN STOCK</span>
          )}
          {item.stock > 0 && item.stock < 20 && (
            <strong style={{ color: 'orange', marginLeft: '10px' }}>¡Reabastecer pronto!</strong>
          )}
        </li>
      ))}
    </ul>
  )}
</section>
```

*(Adjuntar captura de la interfaz con los badges de colores e indicadores de advertencia)*

---

### Ejercicio 12 — Relación anidada en la investigación propia

**Respuesta:**
Se representó la receta de las pizzas (`Pizza` con sus `Ingredientes` asociados mediante el modelo intermedio `RecetaPizza`).

**Código de `App.jsx`:**
```jsx
const recetasPizzas = [
  {
    id: 1,
    pizza: "Pizza Pepperoni Especial",
    ingredientes: [
      { id: 101, nombre: "Masa Tradicional", cantidad: 1, costo: 5.0 },
      { id: 102, nombre: "Queso Mozzarella", cantidad: 200, costo: 8.0 },
      { id: 103, nombre: "Pepperoni Slice", cantidad: 100, costo: 7.5 }
    ]
  },
  {
    id: 2,
    pizza: "Pizza Margarita",
    ingredientes: [
      { id: 201, nombre: "Masa Tradicional", cantidad: 1, costo: 5.0 },
      { id: 202, nombre: "Salsa de Tomate Especial", cantidad: 150, costo: 4.0 },
      { id: 203, nombre: "Queso Mozzarella", cantidad: 180, costo: 7.2 }
    ]
  }
];

// DENTRO DEL JSX:
<section className="seccion-recetas">
  <h2>Composición de Recetas (Relación N:M)</h2>
  {recetasPizzas.map((receta) => {
    const costoTotalReceta = receta.ingredientes.reduce((sum, ing) => sum + ing.costo, 0);
    return (
      <div key={receta.id} className="card-receta" style={{ backgroundColor: '#f9f9f9', padding: '15px', marginBottom: '15px', borderRadius: '8px' }}>
        <h3>{receta.pizza}</h3>
        <p><strong>Ingredientes requeridos ({receta.ingredientes.length}):</strong></p>
        <ul>
          {receta.ingredientes.map((ing) => (
            <li key={ing.id}>
              {ing.nombre} — Cantidad: {ing.cantidad} | Costo aprox: S/ {ing.costo.toFixed(2)}
            </li>
          ))}
        </ul>
        <p style={{ color: '#2c3e50', fontWeight: 'bold' }}>Costo Total de Insumos: S/ {costoTotalReceta.toFixed(2)}</p>
      </div>
    );
  })}
</section>
```

*(Adjuntar captura de las tarjetas de recetas mostrando el listado de ingredientes y el costo total de insumos por pizza)*

---

### Ejercicio 13 — Verificar la interfaz de la investigación propia

**Respuesta:**
Se verificó que la consola del navegador web no mostrara ningún tipo de *Warning* ni error de keys únicas. Se ejecutaron las herramientas de linters y empaquetado final.

- Comandos ejecutados:
  ```powershell
  npm run lint
  npm run build
  ```

**Verificación de exclusión en Git:**
Se comprobó que las carpetas `node_modules/` y `dist/` se encuentren listadas dentro de `.gitignore` para evitar su subida al repositorio remoto de GitHub.

*(Adjuntar capturas de: 1. Consola del navegador sin errores ni advertencias; 2. Terminal ejecutando `npm run lint` y `npm run build` con éxito)*