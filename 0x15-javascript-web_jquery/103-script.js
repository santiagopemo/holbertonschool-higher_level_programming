function makeRequest () {
  $.ajax({
    url: 'https://www.fourtonfish.com/hellosalut/',
    data: { lang: $('INPUT#language_code').val() },
    success: (data) => {
      $('DIV#hello').text(data.hello);
    }
  });
}
$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    makeRequest();
  });
  $('INPUT#language_code').keypress((event) => {
    const keycode = (event.keyCode ? event.keyCode : event.which);
    if (keycode === 13) {
      makeRequest();
    }
  });
});
