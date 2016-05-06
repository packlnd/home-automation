$(function() {
  $('.timepicker').wickedpicker();
  $("#inputtime").on("change", function() {
    console.log('aa');
  });
  $("#buttontime").on('click', function() {
    var time = $('.timepicker').wickedpicker('time');
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
  $.ajax({
    type: "GET",
    url: "/stats",
    success: function(data) {
      console.log(data);
      $("#stats").html(JSON.stringify(data));
    }
  });
});
