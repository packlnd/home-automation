$(function() {
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
