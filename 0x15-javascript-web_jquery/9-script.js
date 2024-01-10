$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, response) {
    $('DIV#hello').text(data.hello);
});