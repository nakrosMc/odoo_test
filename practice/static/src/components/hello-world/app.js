/** @odoo-module **/

import { Component, App } from "@odoo/owl"; 

export class Root extends Component {
    static template = "practice.root";
}

// 1. Función de Montaje
function mountRootComponent() {
    const target = document.getElementById("hello_mount");

    if (target) {
        // 2. 1. Crear la instancia de la aplicación
        const app = new App(Root, {}); // Usa la clase Root definida arriba

        // 2. 2. Montar la instancia en el target
        app.mount(target); 
        
        console.log("Instancia de App creada y componente Owl montado en #hello_mount.");
    } else {
        console.error("El punto de montaje #hello_mount no se encontró en el DOM."); 
    }
}

// 3. Ejecución: Esperar a que el DOM esté listo
window.addEventListener('DOMContentLoaded', mountRootComponent);