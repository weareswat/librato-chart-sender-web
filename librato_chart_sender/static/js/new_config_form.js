jQuery.fn.ForceNumericOnly =
function()
{
    return this.each(function()
    {
        $(this).keydown(function(e)
        {
            var key = e.charCode || e.keyCode || 0;
            // allow backspace, tab, delete, enter, arrows, numbers and keypad numbers ONLY
            // home, end, period, and numpad decimal
            return (
                key == 8 ||
                key == 9 ||
                key == 13 ||
                key == 46 ||
                key == 110 ||
                key == 190 ||
                (key >= 35 && key <= 40) ||
                (key >= 48 && key <= 57) ||
                (key >= 96 && key <= 105));
        });
    });
};
function prevent_submit_on_enter() {
    $("#form-submit-button").click(function() {
        $('#new-config-form').submit();
    });
}

function prevent_duplicates(field_id) {
    $(field_id).on('tokenfield:createtoken', function (event) {
    var existingTokens = $(this).tokenfield('getTokens');
    $.each(existingTokens, function(index, token) {
        if (token.value === event.attrs.value)
            event.preventDefault();
    });
});
}

$( document ).ready(function() {
    prevent_submit_on_enter();
    $('#duration_div').ForceNumericOnly();
    $('#recipients, #chart_ids').tokenfield();
    prevent_duplicates('#recipients, #chart_ids')
});

