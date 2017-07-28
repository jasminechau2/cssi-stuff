function write_user_name_text() {
  var user_name = $("#name_txt").val();
  $("#text_display").text(user_name);
}

function setup() {
  $("#btn_ok").click(write_user_name_text)
}
