function calculate() {
    var Length = parseFloat(document.getElementById('Length').value) || 0;
    var Width = parseFloat(document.getElementById('Width').value) || 0;
    var PricePerCent = parseFloat(document.getElementById('PricePerCent').value) || 0;
    var PlotArea = Length * Width;
    var Cent = PlotArea / 436;
    var Acre = Cent / 100;
    var TotalPrice = Cent * PricePerCent;
    var PricePerSquareFeet = TotalPrice / PlotArea;

    document.getElementById('PlotArea').value = PlotArea.toFixed(2);
    document.getElementById('Cent').value = Cent.toFixed(2);
    document.getElementById('Acre').value = Acre.toFixed(2);
    document.getElementById('TotalPrice').value = TotalPrice.toFixed(2);
    document.getElementById('PricePerSquareFeet').value = PricePerSquareFeet.toFixed(2);
}

function LandResaleCreate(){
    let Length = document.getElementById('Length').value;
    let Width = document.getElementById('Width').value;
    let PlotArea = document.getElementById('PlotArea').value;
    let Cent = document.getElementById('Cent').value;
    let Acre = document.getElementById('Acre').value;
    let District = document.getElementById('District').value;
    let Town = document.getElementById('Town').value;
    let Street = document.getElementById('Street').value;
    let PricePerCent = document.getElementById('PricePerCent').value;
    let TotalPrice = document.getElementById('TotalPrice').value;
    let PricePerSquareFeet = document.getElementById('PricePerSquareFeet').value;
    let Description = document.getElementById('Description').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;


        if(Length == "" || Width == "" || District == "" || Town == "" || Street == "" || PricePerCent == "" ||
             Description == "" || PrimaryNumber == "" || SecondaryNumber == "")
        {
            alert("Please fill the Required fields");
        }
        else{
            $.ajax({
                url : 'land_resale_create/',
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
                    PricePerCent : PricePerCent,
                    TotalPrice : TotalPrice,
                    PricePerSquareFeet : PricePerSquareFeet,
                    Description : Description,
                    PrimaryNumber : PrimaryNumber,
                    SecondaryNumber : SecondaryNumber,
                    csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
                },
                success:function(){
                    alert('The Insert SuccessFully😊');
                },
                error:function(){
                    alert('Some Error Occur');
                }
            });
        }
    }


document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.view').forEach(function(element) {
        element.addEventListener('click', function() {
            var id = this.getAttribute('name');
            window.location.href = "land_view/" + id;
        });
    });
});