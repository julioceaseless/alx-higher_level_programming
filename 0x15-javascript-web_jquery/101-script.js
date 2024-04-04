/*
 * JavaScript script adds, removes and clears LI
 * elements from a list when the user clicks
 */

/* check if DOM is ready */
$('document').ready(function () {
  /* add event listener to click to add element */
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });

  /* add another event listener to remove element */
  $('DIV#remove_item').click(() => {
    $('UL.my_list li:last').remove();
  });

  /* add another event listener to clear elements */
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
