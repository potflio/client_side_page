function ResidentialLeaseCreate(){
    let BhkType = document.getElementById('BhkType').value;
    let Floor = document.getElementById('Floor').value;
    let HouseType = document.getElementById('HouseType').value;
    let Parking = document.getElementById('Parking').value;
    let Terrace = document.getElementById('Terrace').value;
    let Hall = document.getElementById('Hall').value;
    let Bedroom = document.getElementById('Bedroom').value;
    let Bathroom = document.getElementById('Bathroom').value;
    let District = document.getElementById('District').value;
    let Town = document.getElementById('Town').value;
    let Street = document.getElementById('Street').value;
    let ExpectedLease = document.getElementById('ExpectedLease').value;
    let ExpectedLeaseDuration = document.getElementById('ExpectedLeaseDuration').value;
    let Maintenance = document.getElementById('Maintenance').value;
    let Terms = document.getElementById('Terms').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;

    if(BhkType == "" || Floor == "" || HouseType == "" || Parking == "" || Terrace == "" || Hall == "" || 
        Bedroom == "" || Bathroom == "" || District == "" || Town == "" || Street == "" ||
        ExpectedLease == "" || ExpectedLeaseDuration == "" || Maintenance == "" || Terms == "" ||
       PrimaryNumber == "" || SecondaryNumber == ""){

        alert("Please fill the Required Fields");
    }else{
        $.ajax({
            url : 'residential_lease_create/',
            type : 'POST',
            data : {
                BhkType : BhkType,
                Floor : Floor,
                HouseType : HouseType,
                Parking : Parking,
                Terrace : Terrace,
                Hall : Hall,
                Bedroom : Bedroom,
                Bathroom : Bathroom,
                District : District,
                Town : Town,
                Street : Street,
                ExpectedLease : ExpectedLease,
                ExpectedLeaseDuration : ExpectedLeaseDuration,
                Maintenance : Maintenance,
                Terms : Terms,  
                PrimaryNumber : PrimaryNumber,
                SecondaryNumber : SecondaryNumber,
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                alert("Your Property is Posted Successfully😊")
            },
            error:function(){
                alert("Sorry something went Wrong😖");
            }
           
        });
    }

}