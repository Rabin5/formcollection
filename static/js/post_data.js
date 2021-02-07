function saveData(form, modal_id, win_reload) {
    // window.location.reload();
    // var form = $(this);
    // console.log(form, form[0])
    var formdata = new FormData(form[0]);
    action = form.attr('action')

    fetch(action, {
        method: form.attr("method"),
        body: formdata
    })
        .then(function (response) {
            console.log(response)
            if (win_reload) {
                window.location.reload();
            }
            else {
                if (response.redirected == false) {
                    response.text().then(function (data) {
                        $(modal_id).find('.modal-content').html(data)
                    });
                } else {
                    window.location.replace(response['url'])
                }
            }
        })
        .catch(function (err) {
            console.log(err);
        });
    return false;
}
