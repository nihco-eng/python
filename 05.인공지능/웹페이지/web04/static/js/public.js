$("[name='hour']").on("input", function () {
    let value = $(this).val();
    value = value.replace(/[^0-9.]/g, '');
    value = value.replace(/(\..*?)\..*/g, '$1');
    $(this).val(value);
});