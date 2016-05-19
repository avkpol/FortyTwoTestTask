
$(document).ready(function(){
   //code  to solve problem with 403 error
    // (http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request?lq=1)
    $.ajaxSetup({
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     }
});

        $('#submit-id-add_button').click(function(e){

             $("fieldset").prop('disabled', true);
             $(this).prop('disabled', true);
            e.preventDefault();

            // get data from within form
            //var data = {};
            //$("#form").serializeArray().map(function(x){data[x.name] = x.value;});

                $.ajax({
                    type: "POST",
                    url: "/hide/",
                    dataType : "json",
                    data:JSON.stringify({
                        name: $("#id_name").val(),
                        last_name: $("#id_last_name").val(),
                        birth_date: $("#id_birth_date").val(),
                        bio: $("#id_bio").val(),
                        email: $("#id_email").val(),
                        jabber: $("#id_jabber").val(),
                        skype: $("#id_skype").val(),

                     success : function(data) {


                    console.log(data);
                },


                error : function() {

                }

            })

        });
    });
});
