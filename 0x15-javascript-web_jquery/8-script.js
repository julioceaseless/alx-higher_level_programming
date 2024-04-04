/*
 * JQuery and AJAX script fetche and lists title for all
 * movies by using API URL
 */
$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  method: 'GET',
  datatype: 'json',
  success: function (data) {
    /* extract movie title from the fetched data */
    const movieTitles = data.results.map((movie) => {
	    return movie.title;
    });
    const listElement = $('UL#list_movies');
    $.each(movieTitles, (index, title) => {
      const listItem = $('<li>' + title + '</li>');
      listElement.append(listItem);
    });
  }
});
