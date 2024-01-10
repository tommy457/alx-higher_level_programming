$(document).ready(function () {
    $('#language_code').keypress(function (event) {
      if (event.which === 13) { $('#btn_translate').click(); }
    });
    $('#btn_translate').click(function () {
        $.get('https://fourtonfish.com/hellosalut/?lang=' +
        $('INPUT#language_code').val(), function (data, responce) {
          $('DIV#hello').text(data.hello);
      });
    });
  });