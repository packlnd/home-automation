$(function () {
    $("lamp").on("click", function() {
        if ($(this).attr("value") == "ON") {
            turn_on();
        } else {
            turn_off();
        }
    });
    function turn_on() {
        $.ajax({
            url:"/on",
            success: function() {
                $("lamp").attr("value") = "OFF";
            }
        });
    }
    function turn_off() {
        $.ajax({
            url:"/off",
            success: function() {
                $("lamp").attr("value") = "ON";
            }
        });
    }
});
