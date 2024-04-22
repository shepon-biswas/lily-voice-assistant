$(document).ready(function(){
    // Display Speak/Command Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-message li:first").text(message);
        $('.siri-message').textillate('start');
    }

    // Display hood after completed a command
    eel.expose(Showhood)
    function Showhood(){
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }
})