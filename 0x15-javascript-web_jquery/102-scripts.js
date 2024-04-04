/*
 * Javascript script that fetches and prints how
 * to say "Hello" depending on the language
 */
$(document).ready(function () {
  /* add click event */
  $('#btn_translate').click(function () {
    /* get language code */
    const languageCode = $('INPUT#language_code').val();

    /* fetch data using AJAX */
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}',
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        $('#hello').text(translation);
      },
      error: function () {
        /* display error message */
        $('#hello').text('Translation not found.');
      }
    });
  });
});
