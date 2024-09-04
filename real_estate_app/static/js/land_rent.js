function calculate(){
    let Length = parseFloat(document.getElementById('Length').value);
    let Width = parseFloat(document.getElementById('Width').value);

    let PlotArea = Length * Width;
    let Cent = PlotArea / 436;
    let Acre = Cent / 100;

    document.getElementById('PlotArea').value = PlotArea.toFixed(2);
    document.getElementById('Cent').value = Cent.toFixed(2);
    document.getElementById('Acre').value = Acre.toFixed(2);
}

function RentCalculator(){
    let ExpectedRent = parseInt(document.getElementById('ExpectedRent').value);
    let ExpectedDepositMonths = parseInt(document.getElementById('ExpectedDepositMonths').value);
    document.getElementById('ExpectedDeposit').value = ExpectedRent * ExpectedDepositMonths;
    
}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.view').forEach(function(element) {
        element.addEventListener('click', function() {
            var id = this.getAttribute('name');
            window.location.href = "land_view/" + id;
        });
    });
});



function LandRentCreate(){
    let Length = document.getElementById('Length').value;
    let Width = document.getElementById('Width').value;
    let PlotArea = document.getElementById('PlotArea').value;
    let Cent = document.getElementById('Cent').value;
    let Acre = document.getElementById('Acre').value;
    let District = document.getElementById('District').value;
    let Town = document.getElementById('Town').value;
    let Street = document.getElementById('Street').value;
    let ExpectedRent = document.getElementById('ExpectedRent').value;
    let ExpectedDepositMonths = document.getElementById('ExpectedDepositMonths').value;
    let ExpectedDeposit = document.getElementById('ExpectedDeposit').value;
    let Terms = document.getElementById('Terms').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;
    // alert(Length)
    // alert(Width)
    // alert(PlotArea)
    // alert(Cent)
    // alert(Acre)
    // alert(District)
    // alert(Town)
    // alert(Street)
    // alert(ExpectedRent)
    // alert(ExpectedDepositMonths)
    // alert(ExpectedDeposit)
    // alert(Terms)
    // alert(PrimaryNumber)
    // alert(SecondaryNumber)

    if(Length == "" || Width == "" || District == "" || Town == "" || Street == "" || ExpectedRent == "" ||
        ExpectedDepositMonths == "" || Terms == "" || PrimaryNumber == "" || SecondaryNumber == "")
        {
            alert('Please Fill the required field🤔');
        }
        else{
            $.ajax({
                url : 'land_rent_create/',
                type : 'POST',
                data : {
                    Length : Length,
                    Width : Width,
                    PlotArea : PlotArea,
                    Cent : Cent,
                    Acre : Acre,
                    District : District,
                    Town : Town,
                    Street : Street,
                    ExpectedRent : ExpectedRent,
                    ExpectedDepositMonths : ExpectedDepositMonths,
                    ExpectedDeposit : ExpectedDeposit,
                    Terms : Terms,
                    PrimaryNumber : PrimaryNumber,
                    SecondaryNumber : SecondaryNumber,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(){
                    alert("Your Property Insert Successfully😊");
                },
                error:function(){
                    alert("Sorry Some Error Occur😖");
                }
            });
        }
}