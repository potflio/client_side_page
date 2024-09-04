function RentCalculator(){
    let ExpectedRent = parseInt(document.getElementById('ExpectedRent').value);
    let ExpectedDepositMonths = parseInt(document.getElementById('ExpectedDepositMonths').value);
    document.getElementById('ExpectedDeposit').value = ExpectedRent * ExpectedDepositMonths;
    
}

function ResidentialRentCreate(){
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
    let ExpectedRent = document.getElementById('ExpectedRent').value;
    let ExpectedDepositMonths = document.getElementById('ExpectedDepositMonths').value;
    let ExpectedDeposit = document.getElementById('ExpectedDeposit').value;
    let Maintenance = document.getElementById('Maintenance').value;
    let PreferredTenants = document.getElementById('PreferredTenants').value;
    let Terms = document.getElementById('Terms').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;

    if(BhkType == "" || Floor == "" || HouseType == "" || Parking == "" || Terrace == "" || Hall == "" ||
        Bedroom == "" || Bathroom == "" || District == "" || Town == "" || Street == "" ||
        ExpectedRent == "" || ExpectedDepositMonths == "" || ExpectedDeposit == "" || Maintenance == "" || PreferredTenants == "" || Terms == "" ||
        PrimaryNumber == "" || SecondaryNumber == ""){

        alert("Please fill the Required Fields");
    }else{
        $.ajax({
            url : 'residential_rent_create/',
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
                ExpectedRent : ExpectedRent,
                ExpectedDepositMonths : ExpectedDepositMonths,
                ExpectedDeposit : ExpectedDeposit,
                Maintenance : Maintenance,
                PreferredTenants : PreferredTenants,
                Terms : Terms,
                PrimaryNumber : PrimaryNumber,
                SecondaryNumber : SecondaryNumber,
                csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
            },
            success:function(){
                alert("Your Property is Posted Successfully😊");
                window.location.href = "{% url 'index' %}"; 

            },
            error:function(){
                alert("Sorry something went Wrong😖");
            }
           
        });
    }
    alert('Processing....');

}



