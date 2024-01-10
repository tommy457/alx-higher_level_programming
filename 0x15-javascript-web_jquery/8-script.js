$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, response) {
  $.each(data.results, function (index, element) {
    $('#list_movies').append(element.title + '</br>');
  });
});