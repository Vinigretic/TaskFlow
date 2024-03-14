/**
 * Attaches an event listener to the 'DOMContentLoaded' event of the document.
 * When the DOM content is loaded, it selects all elements with the class 'toggle-row'
 * and adds a click event listener to each of them.
 */
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

/**
 * Attaches an event listener to each found checkbox element.
 * When the checkbox is changed, it runs a function to find the form element,
 * then submits the form.
 */

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


