$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    $.ajax({
      url: 'https://www.fourtonfish.com/hellosalut/',
      data: { lang: $('INPUT#language_code').val() },
      success: (data) => {
        $('DIV#hello').text(data.hello);
      }
    });
  });
});
