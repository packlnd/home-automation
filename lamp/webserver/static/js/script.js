$(function () {
    $("lamp").on("click", function() {
        if ($(this).attr("value") == "ON") {
            turn_on();
        } else {
            turn_off();
        }
    });
    function turn_on() {
        // Ajax call
        $("lamp").attr("value") = "OFF";
    }
    function turn_off() {
        // Ajax call
        $("lamp").attr("value") = "ON";
    }
});
