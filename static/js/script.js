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




