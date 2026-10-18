import './App.css';

const IGV = 0.18;

const pizzas = [
  { id: 1, nombre: 'Pizza Pepperoni', precio_base: '28.50', disponible: true },
  { id: 2, nombre: 'Pizza Hawaiana', precio_base: '26.00', disponible: true },
  { id: 3, nombre: 'Pizza Suprema', precio_base: '32.00', disponible: false },
  { id: 4, nombre: 'Pizza Vegetariana', precio_base: '24.00', disponible: true },
  { id: 5, nombre: 'Pizza Cuatro Quesos', precio_base: '30.50', disponible: false },
];

const pedidos = [
  {
    id: 101,
    cliente: 'Carlos Pérez',
    detalles: [
      { id: 1, pizza: 'Pepperoni', cantidad: 2, subtotal: 57.0 },
      { id: 2, pizza: 'Inka Kola 1.5L', cantidad: 1, subtotal: 10.0 },
    ],
  },
  {
    id: 102,
    cliente: 'Ana Gómez',
    detalles: [{ id: 3, pizza: 'Suprema', cantidad: 1, subtotal: 32.0 }],
  },
];

const ingredientes = [
  { id: 1, nombre: 'Queso Mozzarella', unidad_medida: 'gr', stock: 1500 },
  { id: 2, nombre: 'Salsa de Tomate', unidad_medida: 'ml', stock: 15 },
  { id: 3, nombre: 'Pepperoni', unidad_medida: 'gr', stock: 0 },
  { id: 4, nombre: 'Masa Tradicional', unidad_medida: 'unid', stock: 50 },
  { id: 5, nombre: 'Aceitunas Negras', unidad_medida: 'gr', stock: 8 },
];

const repartidores = [
  { id: 1, nombre: 'Juan Pérez', telefono: '987654321', activo: true },
  { id: 2, nombre: 'Maria López', telefono: '912345678', activo: false },
  { id: 3, nombre: 'Carlos Ruiz', telefono: '955555555', activo: true },
];

const recetasPizzas = [
  {
    id: 1,
    pizza: 'Pizza Pepperoni Especial',
    ingredientes: [
      { id: 101, nombre: 'Masa Tradicional', cantidad: 1, costo: 5.0 },
      { id: 102, nombre: 'Queso Mozzarella', cantidad: 200, costo: 8.0 },
      { id: 103, nombre: 'Pepperoni Slice', cantidad: 100, costo: 7.5 },
    ],
  },
  {
    id: 2,
    pizza: 'Pizza Margarita',
    ingredientes: [
      { id: 201, nombre: 'Masa Tradicional', cantidad: 1, costo: 5.0 },
      { id: 202, nombre: 'Salsa de Tomate Especial', cantidad: 150, costo: 4.0 },
      { id: 203, nombre: 'Queso Mozzarella', cantidad: 180, costo: 7.2 },
    ],
  },
];

function App() {
  const precioBase = 25.0;
  const calcularPrecioTotal = (precio) => (precio * (1 + IGV)).toFixed(2);

  return (
    <main className="app-shell">
      <header className="hero">
        <div className="hero-content">
          <p className="eyebrow">Gestión de pizzería · Laboratorio 09</p>
          <h1>Pizzería Gran Sabor</h1>
          <p className="hero-description">
            Menú, pedidos e inventario reunidos en una sola interfaz React.
          </p>
          <div className="price-summary">
            <span>Precio base familiar: S/ {precioBase.toFixed(2)}</span>
            <span>Con IGV (18%): S/ {calcularPrecioTotal(precioBase)}</span>
          </div>
        </div>
        <div className="hero-mark" aria-hidden="true">🍕</div>
      </header>

      <div className="content">
        <section className="section-block" aria-labelledby="catalog-title">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Nuestra carta</p>
              <h2 id="catalog-title">Catálogo de Pizzas</h2>
            </div>
            <span className="count-label">{pizzas.length} variedades</span>
          </div>
          {pizzas.length === 0 ? (
            <p className="empty-state">No hay registros de pizzas disponibles.</p>
          ) : (
            <ul className="pizza-grid">
              {pizzas.map((pizza) => (
                <li key={pizza.id} className="pizza-card">
                  <div className="pizza-card-top">
                    <span className="pizza-emoji" aria-hidden="true">🍕</span>
                    {pizza.disponible ? (
                      <span className="badge badge-available">Disponible</span>
                    ) : (
                      <span className="badge badge-unavailable">Agotado</span>
                    )}
                  </div>
                  <h3>{pizza.nombre}</h3>
                  <p className="price">S/ {Number(pizza.precio_base).toFixed(2)}</p>
                  {!pizza.disponible && (
                    <em className="stock-note">¡Agotado temporalmente!</em>
                  )}
                </li>
              ))}
            </ul>
          )}
        </section>

        <section className="section-block" aria-labelledby="orders-title">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Ventas recientes</p>
              <h2 id="orders-title">Registro de Pedidos</h2>
            </div>
            <span className="count-label">{pedidos.length} pedidos</span>
          </div>
          <div className="orders-grid">
            {pedidos.map((pedido) => {
              const totalPedido = pedido.detalles.reduce(
                (total, item) => total + item.subtotal,
                0,
              );

              return (
                <article key={pedido.id} className="order-card">
                  <div className="order-heading">
                    <div>
                      <span className="order-number">Pedido #{pedido.id}</span>
                      <h3>{pedido.cliente}</h3>
                    </div>
                    <span className="order-icon" aria-hidden="true">🧾</span>
                  </div>
                  <ul className="detail-list">
                    {pedido.detalles.map((detalle) => (
                      <li key={detalle.id}>
                        <span>{detalle.cantidad} × {detalle.pizza}</span>
                        <span>S/ {detalle.subtotal.toFixed(2)}</span>
                      </li>
                    ))}
                  </ul>
                  <div className="order-total">
                    <span>Total del pedido</span>
                    <strong>S/ {totalPedido.toFixed(2)}</strong>
                  </div>
                </article>
              );
            })}
          </div>
        </section>

        <section className="section-block" aria-labelledby="inventory-title">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Investigación propia</p>
              <h2 id="inventory-title">Control de Stock de Ingredientes</h2>
            </div>
            <span className="count-label">{ingredientes.length} ingredientes</span>
          </div>
          {ingredientes.length === 0 ? (
            <p className="empty-state">No hay ingredientes registrados en la base de datos.</p>
          ) : (
            <ul className="inventory-list">
              {ingredientes.map((item) => (
                <li key={item.id} className="inventory-item">
                  <div className="inventory-info">
                    <strong>{item.nombre}</strong>
                    <span>{item.stock} {item.unidad_medida}</span>
                  </div>
                  <div className="inventory-status">
                    {item.stock === 0 ? (
                      <span className="badge badge-unavailable">Agotado</span>
                    ) : (
                      <span className="badge badge-available">En stock</span>
                    )}
                    {item.stock > 0 && item.stock < 20 && (
                      <strong className="restock-note">¡Reabastecer pronto!</strong>
                    )}
                  </div>
                </li>
              ))}
            </ul>
          )}
        </section>

        <section className="section-block" aria-labelledby="couriers-title">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Equipo de reparto</p>
              <h2 id="couriers-title">Repartidores</h2>
            </div>
            <span className="count-label">{repartidores.length} repartidores</span>
          </div>
          <ul className="courier-grid">
            {repartidores.map((repartidor) => (
              <li key={repartidor.id} className="courier-card">
                <div className="avatar" aria-hidden="true">
                  {repartidor.nombre.charAt(0)}
                </div>
                <div className="courier-info">
                  <strong>{repartidor.nombre}</strong>
                  <span>{repartidor.telefono}</span>
                </div>
                {repartidor.activo ? (
                  <span className="badge badge-available">Activo</span>
                ) : (
                  <span className="badge badge-inactive">Inactivo</span>
                )}
              </li>
            ))}
          </ul>
        </section>

        <section className="section-block" aria-labelledby="recipes-title">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Relación N:M</p>
              <h2 id="recipes-title">Composición de Recetas</h2>
            </div>
            <span className="count-label">{recetasPizzas.length} recetas</span>
          </div>
          <div className="recipes-grid">
            {recetasPizzas.map((receta) => {
              const costoTotalReceta = receta.ingredientes.reduce(
                (total, ingrediente) => total + ingrediente.costo,
                0,
              );

              return (
                <article key={receta.id} className="recipe-card">
                  <h3>{receta.pizza}</h3>
                  <p className="recipe-caption">
                    Ingredientes requeridos ({receta.ingredientes.length})
                  </p>
                  <ul className="recipe-list">
                    {receta.ingredientes.map((ingrediente) => (
                      <li key={ingrediente.id}>
                        <span>
                          {ingrediente.nombre}
                          <small>Cantidad: {ingrediente.cantidad}</small>
                        </span>
                        <span>S/ {ingrediente.costo.toFixed(2)}</span>
                      </li>
                    ))}
                  </ul>
                  <div className="recipe-total">
                    <span>Costo total de insumos</span>
                    <strong>S/ {costoTotalReceta.toFixed(2)}</strong>
                  </div>
                </article>
              );
            })}
          </div>
        </section>
      </div>

      <footer className="page-footer">
        <span>Pizzería Gran Sabor</span>
        <span>Interfaz demostrativa · React + Vite</span>
      </footer>
    </main>
  );
}

export default App;
