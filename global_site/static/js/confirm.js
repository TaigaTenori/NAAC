function deleteConfirm(url) {
    event.preventDefault();
    console.log(url)
    Swal.fire({
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
      if (result.value) {
        location.href = url;
      }
    })
}
async function emailChangeConfirm() {
    event.preventDefault();
    const { value: email } = await Swal.fire({
      title: 'Input email address',
      input: 'email',
      inputPlaceholder: 'Enter your email address'
    })

    if (email) {
        console.log('ajax');
        $.ajax({
            url: '/ajax/change_email/',
            data: {
              'new_email': email
            },
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                  var cell = $('#change_email');
                  cell.html = email;
                  cell.fadeOut(800, function(){
                      $('#change_email').html(email).fadeIn().delay(2000);

                  });

                }
                //Swal.fire("E-mail changed successfully!");
              }
            }
          );
    }
}
