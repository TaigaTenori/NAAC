function deleteConfirm(url) {
    event.preventDefault();
    
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
async function passwordChange() {
  event.preventDefault();

  const { value: new_password } = await Swal.fire({
    title: 'Password Change',
    input: 'password',
    inputPlaceholder: 'Enter your new password',
  })
  const { value: new_password2 } = await Swal.fire({
    title: 'Repeat password',
    input: 'password',
    inputPlaceholder: 'Repeat your new password',
})

    if (new_password && (new_password == new_password2)) {
        console.log('ajax');
        $.ajax({
            url: '/ajax/change_password/',
            data: {
              'new_password': new_password
            },
            dataType: 'json',
            success: function (data) {
                if (data.success) {
                  var cell = $('#change_password');
                  cell.html('Password changed');
                  cell.fadeOut(1800, function(){
                      $('#change_password').html('************').fadeIn().delay(3000);

                  });

                }
              }

            }
        ).fail(function(jqXHR, textStatus, error) {

        });
    }
    else {
        Swal.fire({
        title: 'Error',
        text: "Passwords do not match",
        icon: 'warning'
        });
    }
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
              }
            }
          );
    }
}
