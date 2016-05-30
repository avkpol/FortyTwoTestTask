function imageIsLoaded(e) {
    $('#photo-preview').attr('width', "200px");
    $('#photo-preview').attr('src', e.target.result);


}

$(document).ready(function(){
    $("#photo-clear_id").remove();
    $(".controls label").remove();


    $("#id_photo").change(function () {

        if (this.files && this.files[0]) {
            var reader = new FileReader();
            reader.onload = imageIsLoaded;
            reader.readAsDataURL(this.files[0]);
        }
    });
    //disable button after submit (need to be corrected)

$('#s1-btn').click(function(e) {
        e.preventDefault();
        $(this).prop('disabled', true)
        $.post(
            "/run-key-gen-process/",
            onAjaxSuccess
        );

        function onAjaxSuccess(data) {
            if (data == "Key was succesfully generated an tested!") {
                $("#jmessage").addClass("alert alert-success")
                    .text(data).fadeOut(6000);
            }
            $('#s1-btn').click(function() {


                $("#jmessage").removeClass("alert alert-success").addClass("alert alert-info")
                    .text("Button is disabled since you already generated and tested the key");
            });
        };
    });

//   //code  to solve problem with 403 error
//    // (http://stackoverflow.com/questions/5100539/django-csrf-check-failing-with-an-ajax-post-request?lq=1)
//    $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         function getCookie(name) {
//             var cookieValue = null;
//             if (document.cookie && document.cookie != '') {
//                 var cookies = document.cookie.split(';');
//                 for (var i = 0; i < cookies.length; i++) {
//                     var cookie = jQuery.trim(cookies[i]);
//                     // Does this cookie string begin with the name we want?
//                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
//                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                         break;
//                     }
//                 }
//             }
//             return cookieValue;
//         }
//         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
//             // Only send the token to relative URLs i.e. locally.
//             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
//         }
//     }
//});

    //    $('#submit-id-add_button').click(function(e){
    //
    //         $("fieldset").prop('disabled', true);
    //         $(this).prop('disabled', true);
    //        e.preventDefault();
    //
    //        // get data from within form
    //        //var data = {};
    //        //$("#form").serializeArray().map(function(x){data[x.name] = x.value;});
    //
    //            $.ajax({
    //                type: "POST",
    //                url: "/hide/",
    //                dataType : "json",
    //                data:JSON.stringify({
    //                    name: $("#id_name").val(),
    //                    last_name: $("#id_last_name").val(),
    //                    birth_date: $("#id_birth_date").val(),
    //                    bio: $("#id_bio").val(),
    //                    email: $("#id_email").val(),
    //                    jabber: $("#id_jabber").val(),
    //                    skype: $("#id_skype").val(),
    //
    //                 success : function(data) {
    //
    //
    //                console.log(data);
    //            },
    //
    //
    //            error : function() {
    //
    //            }
    //
    //        })
    //
    //    });
    //});

    $('#submit-id-save_changes').click(function(e) {
        var options = {
            target:     '#photo-preview', // div to update
            url:        '/save_image/',
            beforeSubmit: function() {
                $('#submit-id-save_changes').prop("disabled", true);
                $('#loader').show();
            },
            success:    function(data) {

                var new_url = $('#id_photo')[0].value.replace("C:\\fakepath\\", "photo/");
                $(".controls a").attr("href", "/static/media/" + new_url);
                $(".controls a").html( new_url);
                 $('#submit-id-save').prop("disabled", false);

            $('#loader').hide();
            $('.success-message').html('<p class="alert alert-success" role="alert"> Changes have been saved!</p>')
                .fadeOut(6000);
                //alert("data saved!")

            }
        };

         $('#data-fields').ajaxForm(options);
             //$('#img1').attr("src", "https://pm-content.cdn.prismic.io/pm-content/f5d1d11406475b05ae56e6c33972d51918ee00aa_picmonkey_home_01.jpg");

//    var editForm = $('#submit-id-save');
//
//    var options = {
//        url:        '/save_image/',
//        target: "panel-body",
//        beforeSubmit: function(){
//            $('#submit-id-save:input').prop("disabled", true);
//            //$('#loader').show();
//        },
//        success: function(){
//            $('#submit-id-save').prop("disabled", false);
//            $('html,body').scrollTop(0);
//            $('#loader').hide();
//            $('.msg').html('<p class="alert alert-success" role="alert"><strong>Success!</strong> Changes have been saved!</p>');
//        }
//    };
//
//    editForm.ajaxForm(options);
//    alert('lllll')
//
//
//
//
//    function readURL(input) {
//    if (input.files && input.files[0]) {
//        var reader = new FileReader();
//            reader.onload = function (e) {
//                $('#photo-preview').attr('src', e.target.result);
//            }
//        reader.readAsDataURL(input.files[0]);
//    }
//}
//$("#id_photo").change(function(){readURL(this);});
//             //alert("Thank you for your comment!");
//

        //
        //e.preventDefault();
        //$.ajax({
        //    type: "POST",
        //    url: "/display_image/",
        //    dataType: "jpg",
        //    data:""
        });
       });




