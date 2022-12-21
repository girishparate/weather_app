$("#pass").keyup(function(){
    var password = $(this).val().trim()
    var password_conf = $("#confirm_pass").val().trim()
    if (password===password_conf && password.length !==0){
      console.log(password, password_conf)
        $("#registration_submit").prop("disabled", false);
    }
  });

  $("#confirm_pass").keyup(function(){
    var password = $("#pass").val().trim()
    var password_conf = $(this).val().trim()
    
    if (password===password_conf && password_conf.length !==0){
      console.log(password, password_conf)
        $("#registration_submit").prop("disabled", false);
    }
  });