function email_send(){
    let email = document.getElementById('email').value;
    if(email == ""){
        alert("Please fill the required Field");
    }else{
        $.ajax({
            url : 'send/',
            type : 'POST',
            data : {
                email : email,
                csrfmiddlewaretoken : $('input[name=csrfmiddletoken]').val()
            },
            success:function(response){
                if(response.status === 'success'){
                    alert('Success');
                }
            },
            error:function(xhr, status, error){
                //alert("Some Error Occurs");
                console.log('Error:', error);
            }
        });
    }
}

function send_otp(){
    let otp = document.getElementById('otp').value;
    if(otp == ""){
        alert("Please fill the required Field");
    }
    else{
        $.ajax({
            url : 'verification/',
            type : 'POST',
            data : {
                otp : otp,
                csrfmiddlewaretoken : $('input[name = csrfmiddletoken]').val()
            },
            success:function(){
                alert("Your Login Successfully");
            },
            error:function(){
                alert("Some Error Occurs");
            }
        })
    }
}