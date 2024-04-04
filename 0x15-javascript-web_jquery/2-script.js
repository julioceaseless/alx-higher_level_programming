/* jQuery script to update text color of header */
$(document).ready(function () {
  const redHeaderDiv = $('DIV#red_header');
  redHeaderDiv.click(function () {
    /* find the header */
    const headerElem = $('header');
    /* change color if element found */
    if (headerElem) {
      headerElem.css('color', 'red');
    } else {
      console.error('Header elemnet not found');
    }
  });
});
