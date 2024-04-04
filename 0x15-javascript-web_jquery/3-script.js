/* jQuery script to add class to header element */
$(document).ready(function () {
  const redHeaderDiv = $('DIV#red_header');
  redHeaderDiv.click(function () {
    const headerElem = $('header');
    if (headerElem) {
      headerElem.addClass('red');
    } else {
      console.error('Header elemnet not found');
    }
  });
});
