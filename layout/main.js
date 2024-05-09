$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri Wave Script
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.3,
        autostart: true
    });

    // Siri message animation
    $('.siri-message').textillate({
        // loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () { 
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
    });

    function docKeyUp(e) {
        if (e.key === 'j' && e.metaKey) {
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', docKeyUp, false);


    //   chat assisatnt- commands by message
    function ChatAssistant(MgsCommands) {

        if (MgsCommands != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(MgsCommands);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }
    // toogle fucntion to hide and display mic and send button 
    function ToggleSendButton(MgsCommands) {
        if (MgsCommands.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {
        let MgsCommands = $("#chatbox").val();
        ToggleSendButton(MgsCommands)
    });
    
    // send button event handler
    $("#SendBtn").click(function () { 
        let MgsCommands = $("#chatbox").val()
        ChatAssistant(MgsCommands)
    });

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let MgsCommands = $("#chatbox").val()
            ChatAssistant(MgsCommands)
        }
    });
})