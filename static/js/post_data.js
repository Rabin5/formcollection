function saveData(form,modal_id){
    // var form = $(this);
    // console.log(form, form[0])
    var formdata = new FormData(form[0])
    fetch(form.attr('action'), {
        method: form.attr("method"),
        body: formdata
    })
    .then(function(response){
        console.log(response)
        response.text().then(function(data){
            console.log(data)
            $(modal_id).find('.modal-content').html(data)
   
        });
        // window.location.reload();
    })
    .catch(function(err){
        console.log(err);    
    });
    return false;
}