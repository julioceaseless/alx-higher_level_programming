/*
 * JQuery script to toggle oggles the class of the <header> element
 * when the user clicks on the tag DIV#toggle_header
 */
$(document).ready(function () {
  /* select div */
  const toggleDiv = $('DIV#toggle_header');
  const headerElem = $('header');

  // add a click event handler
  toggleDiv.click(function () {
    headerElem.toggleClass('red green');
  });
});
