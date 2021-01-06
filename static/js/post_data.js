function saveData(form){
    // var form = $(this);
    // console.log(form, form[0])
    var formdata = new FormData(form[0])
    fetch(form.attr('action'), {
        method: form.attr("method"),
        body: formdata
    })
    .then(function(response){
        window.location.reload();
    })
    .catch(function(err){
        console.log(err);
    });
    return false;
}