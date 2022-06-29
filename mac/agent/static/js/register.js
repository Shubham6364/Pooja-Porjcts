$(document).ready(function() {
     $(".form").validate();
});

$(".toggle-password").click(function() {
   $(this).toggleClass("fa-eye fa-eye-slash");
    var input = $($(this).attr("toggle"));
    if (input.attr("type") == "password") {
        input.attr("type", "text");
    } else {
            input.attr("type", "password");
    }
});

$(function() {
   $('#username').on('keypress', function(e) {
      if (e.which == 32){
         return false;
      }
   });
   $('#fname').on('keypress', function(e) {
      if (e.which == 32){
         return false;
      }
   });
   $('#lname').on('keypress', function(e) {
      if (e.which == 32){
         return false;
      }
   });
});

function Validate(){
     var pin = document.getElementById("pin").value;
     var cpin = document.getElementById("cpin").value;
     if (pin != cpin) {
         alert("Pin do not match.");
         return false;
     }
     return true;
}

