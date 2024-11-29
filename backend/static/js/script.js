document.addEventListener('DOMContentLoaded', function() {
    // Function to handle card recharge
    function rechargeCard(id_tarjeta, monto) {
        // Simulate an API call to recharge the card
        console.log(`Recargando la tarjeta ${id_tarjeta} con monto ${monto}`);
        // Here you would typically make an AJAX call to your backend API
        // Example:
        // fetch('/api/recharge', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ id_tarjeta: id_tarjeta, monto: monto })
        // }).then(response => response.json())
        // .then(data => {
        //     console.log('Success:', data);
        // }).catch((error) => {
        //     console.error('Error:', error);
        // });
    }

    // Function to handle card sales
    function sellCard(tipo_tarjeta) {
        // Simulate an API call to sell the card
        console.log(`Adquirir tarjeta ${tipo_tarjeta}`);
        // Here you would typically make an AJAX call to your backend API
        // Example:
        // fetch('/api/sell', {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({ tipo_tarjeta: tipo_tarjeta })
        // }).then(response => response.json())
        // .then(data => {
        //     console.log('Success:', data);
        // }).catch((error) => {
        //     console.error('Error:', error);
        // });
    }

    // Event listeners for form submissions
    document.getElementById('rechargeForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const id_tarjeta = document.getElementById('id_tarjeta').value;
        const monto = document.getElementById('monto').value;
        rechargeCard(id_tarjeta, monto);
    });

    document.getElementById('sellForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const tipo_tarjeta = document.getElementById('tipo_tarjeta').value;
        sellCard(tipo_tarjeta);
    });
});