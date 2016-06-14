//loading image and resize 'on the fly' for preview
function imageIsLoaded(e) {
    $('#photo-preview').attr('height',"200px" );
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
// posting form using ajaxForm
    $('#submit-id-save_changes').click(function(e) {
        var options = {
            target:     '#photo-preview', // div to update
            url:        '/save_image/',
            beforeSubmit: function() {
                $('#submit-id-save_changes').prop("disabled", true);
                $('#loader').show(); //show loader.gif
            },
            success:    function() {
            // replace url in current loaded photo
            var new_url = $('#id_photo')[0].value.replace("C:\\fakepath\\", "photo/");
                $(".controls a").attr("href", "/static/media/" + new_url);
                $(".controls a").html( new_url);
                 $('#submit-id-save').prop("disabled", false);

            $('#loader').hide();
            $('.success-message').html('<p class="alert alert-success" role="alert"> Changes have been saved!</p>')
                .fadeOut(6000);
            }
        };
         $('#data-fields').ajaxForm(options);

    });
});




