// Call the dataTables jQuery plugin
var lenguage_config = {
  "language": {
      "lengthMenu": "Display _MENU_ records per page",
      "zeroRecords": "Nada encontrado",
      "info": "Mostrando página _PAGE_ de _PAGES_",
      "infoEmpty": "Não há registros disponíveis",
      "thousands": "",
      "decimal":",",
      "lengthMenu":     "Mostrar _MENU_ linhas",
    "loadingRecords": "Carregando...",
    "processing":     "Processando...",
    "search":         "Buscar:",
    "zeroRecords":    "Não foram encontrados resultados",
    "paginate": {
        "first":      "Primeiro",
        "last":       "Último",
        "next":       "Próximo",
        "previous":   "Anterior"
    },
  }
}

$(document).ready(function() {
  
  $('#myClientsTable').DataTable(lenguage_config);
  $('#myTestsTable').DataTable(lenguage_config);
});

