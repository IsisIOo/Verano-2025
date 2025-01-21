<template>
    <div class="items-for-sale">
      <h1>Objetos en Venta</h1>
      <ul>
        <li v-for="item in items" :key="item.id" class="item">
          <h2>{{ item.name }}</h2>
          <p>{{ item.description }}</p>
          <p><strong>Precio:</strong> ${{ item.price }}</p>
          <button @click="addToCart(item)">Agregar al Carrito</button>
        </li>
        
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ItemsForSale',
    data() {
      return {
        items: [
        { id: 1, name: 'Cámara', description: 'Cámara digital de alta resolución', price: 300 },
        { id: 2, name: 'Laptop', description: 'Laptop con 16GB de RAM y 512GB SSD', price: 1200 },
        { id: 3, name: 'Teléfono', description: 'Teléfono móvil con pantalla AMOLED', price: 800 },
        { id: 4, name: 'Cámara deportiva', description: 'Cámara deportiva sumergible', price: 350 },
        { id: 5, name: 'Tablet', description: 'Tablet con pantalla de 10 pulgadas', price: 600 },
        { id: 6, name: 'Auriculares', description: 'Auriculares con cancelación de ruido', price: 250 },
        { id: 7, name: 'Smartwatch', description: 'Reloj inteligente con monitor de ritmo cardíaco', price: 400 },
        { id: 8, name: 'Impresora', description: 'Impresora multifunción inalámbrica', price: 150 },
        { id: 9, name: 'Teclado', description: 'Teclado mecánico con retroiluminación', price: 100 },
        { id: 10, name: 'Cámara profesional', description: 'Cámara réflex con lentes intercambiables', price: 900 },
        { id: 11, name: 'Monitor', description: 'Monitor 4K UHD de 27 pulgadas', price: 500 },
        { id: 12, name: 'Consola de juegos', description: 'Consola de juegos de última generación', price: 700 },
        { id: 13, name: 'Altavoces', description: 'Altavoces Bluetooth de alta fidelidad', price: 200 }
        ]
      };
    },
    methods: {
      addToCart(item) {
        console.log(`Agregado al carrito: ${item.name}`);
        // Aquí puedes añadir lógica para agregar el ítem al carrito
      }
    }
  };
  </script>

<style scoped>
/* Contenedor principal que envuelve toda la sección de items en venta 
   Establece el área general donde se mostrarán todos los productos */
.items-for-sale {
  padding: 20px;                    /* Agrega 20px de espacio interno en todos los lados */
  background-color: #f9f9f9;        /* Define un color de fondo gris muy claro */
  margin: 0 auto;                   /* Centra el contenedor en la página */
}

/* Estilos para el título principal de la sección 
   Configura cómo se ve el encabezado H1 */
.items-for-sale h1 {
  text-align: left;               /* Centra el texto del título */
  color: #333;                      /* Color gris oscuro para el texto */
  margin-bottom: 10px;              /* Espacio de 20px debajo del título */
}

/* Configuración del contenedor de la lista de items 
   Este es el contenedor flexible que organiza todos los productos */
.items-for-sale ul {
  display: flex;                    /* Activa el modelo de diseño flexbox */
  flex-direction: row;              /* Organiza los elementos en fila (horizontal) */
  flex-wrap: wrap;                  /* Permite que los elementos pasen a la siguiente línea si no hay espacio */
  gap: 20px;                        /* Espacio de 20px entre todos los elementos */
  list-style: none;                 /* Elimina los puntos de la lista */
  padding: 1;                       /* Elimina el relleno predeterminado de la lista */
  justify-content: flex-start;      /* Alinea los elementos desde la izquierda */
  width: fit-content;               /* Hace que el ancho se ajuste al contenido */
  margin: 0 auto;                   /* Centra el contenedor de la lista */
}

/* Estilos para cada tarjeta de producto individual 
   Define cómo se ve cada producto en la cuadrícula */
.item {
  border: 1px solid #f0f;           /* Borde gris claro alrededor de cada item */
  padding: 15px;                    /* Espacio interno de 15px en todos los lados */
  border-radius: 5px;               /* Esquinas redondeadas */
  background-color: #fff;           /* Fondo blanco para cada tarjeta */
  box-sizing: border-box;           /* Incluye padding y border en el ancho total */
  flex: 0 1 250px;                  /* Configuración flexible del item:
                                      - 0: no permite crecer más allá del tamaño base
                                      - 1: permite encogerse si es necesario
                                      - 250px: tamaño base del elemento */
}

/* Estilos para los títulos dentro de cada tarjeta de producto */
.item h2 {
  margin: 0 0 10px;                 /* Elimina margen superior e inferior, 10px abajo */
  color: #42b983;                   /* Color verde para el título */
}

/* Estilos para los párrafos dentro de cada tarjeta de producto */
.item p {
  margin: 5px 0;                    /* Pequeño espacio vertical entre párrafos */
}

/* Estilos para los botones dentro de cada tarjeta */
.item button {
  background-color: #42b983;        /* Color de fondo verde para el botón */
  color: white;                     /* Texto en color blanco */
  border: none;                     /* Elimina el borde del botón */
  padding: 10px 20px;              /* Espacio interno: 10px arriba/abajo, 20px izquierda/derecha */
  cursor: pointer;                 /* Cambia el cursor a una mano al pasar por encima */
  border-radius: 5px;              /* Esquinas redondeadas del botón */
}

/* Efecto al pasar el mouse sobre el botón */
.item button:hover {
  background-color: #358a6b;        /* Cambia a un verde más oscuro al pasar el mouse */
}
</style>