/* jQuery script to change text color */
$(document).ready(function () {
  /* select the div */
  const redDiv = $('DIV#red_header');
  /* add a click event handler */
  redDiv.click(function () {
    /* find the header */
    const headerElem = $('header');
    /* set color */
    if (headerElem) {
      headerElem.css('color', '#FF0000');
    } else {
      console.error('Header elemnet not found');
    }
  });
});
