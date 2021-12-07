window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('myClientsTable');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }

});

window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('myTestsTable');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
});