/*
 * JQuery and AJAX script fetches character name from URL
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  datatype: 'json',
  success: function (data) {
    /* extract name of character from the fetched data */
    const characterName = data.name;

    /* display character's name in the div */
    $('DIV#character').text(characterName);
  }
});
