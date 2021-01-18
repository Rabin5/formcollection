function saveData(form,modal_id){
    // var form = $(this);
    // console.log(form, form[0])
    var formdata = new FormData(form[0])
    formdata.append('body', '1');
    formdata.append('fiscal_year', '1');
    if (action == ''){
        action = form.attr('action')
    }
    fetch(action, {
        method: form.attr("method"),
        body: formdata
    })
    .then(function(response){
        response.text().then(function(data){
            $(modal_id).find('.modal-content').html(data)
        });
    })
    .catch(function(err){
        console.log(err); 
    });
    return false;
}