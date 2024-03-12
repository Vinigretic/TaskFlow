document.addEventListener('DOMContentLoaded', function() {
  var toggleCells = document.querySelectorAll('.toggle-row');

  toggleCells.forEach(function(cell) {
    cell.addEventListener('click', function() {
      var row = this.parentNode;
      var nextRow = row.nextElementSibling;

      if (nextRow.classList.contains('collapse')) {
        nextRow.classList.toggle('show');
      }
    });
  });
});

// Find all the checkboxes on the page
var checkboxes = document.querySelectorAll('.form-check-input');

// For each checkbox add an event handler
checkboxes.forEach(function(checkbox) {
    checkbox.addEventListener('change', function() {
        // Finding form
        var form = checkbox.closest('form');

        // Send the form when the checkbox is changed
        form.submit();
    });
});


