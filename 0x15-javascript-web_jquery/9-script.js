// $.ajax({
//   url: 'https://fourtonfish.com/hellosalut/?lang=fr',
//   success: (data) => {
//     $('DIV#hello').text(data.hello);
//   }
// });
$('document').ready(() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(url, (data) => {
    $('DIV#hello').text(data.hello);
  });
});
