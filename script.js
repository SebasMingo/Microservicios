const apiUrlProductos = 'http://localhost:5000/productos';
const apiUrlPedidos = 'http://localhost:5005/pedidos';

function crearProducto() {
    const nombre = document.getElementById('nombreProducto').value;
    const precio = document.getElementById('precioProducto').value;

    fetch(apiUrlProductos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre: nombre, precio: parseFloat(precio) })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        listarProductos();
    })
    .catch(error => console.error('Error:', error));
}

function listarProductos() {
    fetch(apiUrlProductos)
    .then(response => response.json())
    .then(data => {
        const productosDiv = document.getElementById('productos');
        productosDiv.innerHTML = '<h2>Lista de Productos:</h2>';
        data.forEach(producto => {
            productosDiv.innerHTML += `<p>ID: ${producto[0]}, Nombre: ${producto[1]}, Precio: ${producto[2]}</p>`;
        });
    })
    .catch(error => console.error('Error:', error));
}

function crearPedido() {
    const productos = document.getElementById('productosPedido').value;
    const cantidad = document.getElementById('cantidadPedido').value;

    fetch(apiUrlPedidos, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ productos: productos, cantidad: parseInt(cantidad) })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        listarPedidos();
    })
    .catch(error => console.error('Error:', error));
}

function listarPedidos() {
    fetch(apiUrlPedidos)  // Esto debe ser a http://localhost:5005/pedidos
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        const pedidosDiv = document.getElementById('pedidos');
        pedidosDiv.innerHTML = '<h2>Lista de Pedidos:</h2>';
        data.forEach(pedido => {
            pedidosDiv.innerHTML += `<p>ID: ${pedido[0]}, Productos: ${pedido[1]}, Cantidad: ${pedido[2]}</p>`;
        });
    })
    .catch(error => console.error('Error:', error));
}


// Llamar a listarProductos y listarPedidos al cargar la página
document.addEventListener('DOMContentLoaded', () => {
    listarProductos();
    listarPedidos();
});
