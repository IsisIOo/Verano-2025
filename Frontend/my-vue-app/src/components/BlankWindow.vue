<!-- src/components/BlankWindow.vue -->

<!--Asi era la cosa con solo una clase en la vista-->
<!-- <template>
    <div class = "blank-window">
      <h1>Ventana en Blanco</h1>
      <router-link to="/">Volver a la Página Principal</router-link>
    </div>
  </template>-->

 <!--Asi es la cosa ahora con 2 clases en la misma vista--> 
 <template>
  <div class="blank-window">
    <h1>Ventana en Blanco</h1>
    <router-link to="/">Volver a la Página Principal</router-link>

    <!-- Nueva sección con la clase extra-section -->
    <div class="extra-section">
      <h2>Sección Extra</h2>
      <p>Este es un párrafo dentro de la sección extra.</p>
      <router-link to="/">Volver a la Página Principal desde la Sección Extra</router-link>

      <!--Este es para que los dos link estén separados por salto de linea,sin esto estaban uno al lado del otro--> 
      <div class="spacer"></div>

      <!--Así era el link para que tuviera las mismas propiedades que el link anterior--> 
      <!-- <router-link to="/items-for-sale">Ver Objetos en Venta</router-link>-->

      <!--Asi es para que tenga caracteristicas diferentes al link previo, se agrega class. Notar que está contenido
      dentro de extras-section por identacion-->
      <router-link to="/items-for-sale" class="special-link">Ver Objetos en Venta</router-link>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'BlankWindow'
  }
  </script>
  
  <style scoped>
  /* Estilos específicos para el componente BlankWindow */

  /*Este es el color del fondo */
  .blank-window {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #555;
}

/*Este es el color del texto */
.blank-window h1 {
  color: #db57a4;
  font-size: 2rem;
  margin-bottom: 1rem;
}

/*Este es el color de los enlaces */
.blank-window a {
  color: #42b983;
  text-decoration: none;
  font-size: 1.2rem;
}

/*Este hace que aparezca una linea que subraya los enlaces */
.blank-window a:hover {
  text-decoration: underline;
}

/* Nuevos estilos para la sección extra */
/* Estilos para la clase extra-section */
.extra-section {
  border: 2px solid #42b983; /*Borde y grosor de la sección extra*/
  padding: 20px;  /*Espaciado interno de la sección extra, tamaño del bloque que contiene la seccion extra*/
  margin-top: 20px; /*Espaciado externo de la sección extra, la distancia que tiene desde arriba*/
  background-color: #ffffff; /*Color de fondo de la sección extra*/
  width: 80%; /*Ancho de la sección extra, se estira hacia los lados*/
  text-align: center; /*Alineación del texto en el centro*/
}

.extra-section h2 {
  color: #050; /*Color del titulo h2 de la sección extra*/
  font-size: 1.5rem; /*Tamaño de la fuente del titulo h2 de la sección extra*/
  margin-bottom: 1rem; /*Espaciado inferior del titulo h2 de la sección extra, aleja lo que está debajo de él*/
}

.extra-section p {
  color: #000; /*Color del texto p de la sección extra*/
  font-size: 1rem; /*Tamaño de la fuente del texto p de la sección extra*/
  margin-bottom: 1rem; /*Espaciado inferior del texto p de la sección extra, aleja lo que está debajo de él*/
}

.extra-section a {
  color: #d51212; /*Color de los enlaces de la sección extra*/
  text-decoration: none; /*Quita la subraya de los enlaces de la sección extra*/
  font-size: 1rem; /*Tamaño de la fuente de los enlaces de la sección extra*/
}

.extra-section a:hover {
  text-decoration: underline; /*Subraya los enlaces de la sección extra al pasar el mouse por encima*/
}


/*caracteristicas del segundo link */
.special-link {
  color: #007bff; /* Cambia el color del texto */
  font-weight: bold; /* Hace el texto en negrita */
  background-color: none; /* Fondo gris claro (al no ponerle el mouse encima) */
  padding: 10px 20px; /* Añade padding alrededor del enlace */
  border-radius: 5px; /* Bordes redondeados */
  text-decoration: none; /* Elimina subrayado */
  display: inline-block; /* Para aplicar padding y background correctamente */
}


.special-link:hover {
  background-color: #000; /* Cambia el fondo al pasar el ratón */
  text-decoration: underline; /* Añade subrayado al pasar el ratón */
}
  </style>