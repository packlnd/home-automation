$(function() {
  $('.timepicker').wickedpicker();
  $("#input-time").on('input', function() {
    var time = $("#input-time").text();
    console.log(time);
    $.ajax({
      type: "POST",
      url: "/morning_alarm",
      data: {'time': time},
      success: function(resp) {
        console.log(resp);
      }
    });
  });
  $("#myonoffswitch").on('click', function() {
    console.log(this.checked);
    var ep = this.checked ? "on" : "off";
    $.ajax({
      type: "GET",
      url: "/"+ep,
      success: function(data) {
        console.log(data);
      }
    })
  });
});
