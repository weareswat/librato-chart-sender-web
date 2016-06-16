function prevent_submit_on_enter() {
    $("#form-submit-button").click(function() {
        $('#new-config-form').submit();
    });
}

$( document ).ready(function() {
    $('select').tagsinput('items');
    prevent_submit_on_enter();
});