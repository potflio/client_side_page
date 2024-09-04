function calculate() {
    var Length = parseFloat(document.getElementById('Length').value) || 0;
    var Width = parseFloat(document.getElementById('Width').value) || 0;

    var PlotArea = Length * Width;
    var Cent = PlotArea / 436;
    var Acre = Cent / 100;

    document.getElementById('PlotArea').value = PlotArea.toFixed(2);
    document.getElementById('Cent').value = Cent.toFixed(2);
    document.getElementById('Acre').value = Acre.toFixed(2);
}


function LandLeaseCreate(){
    let Length = document.getElementById('Length').value;
    let Width = document.getElementById('Width').value;
    let PlotArea = document.getElementById('PlotArea').value;
    let Cent = document.getElementById('Cent').value;
    let Acre = document.getElementById('Acre').value;
    let District = document.getElementById('District').value;
    let Town = document.getElementById('Town').value;
    let Street = document.getElementById('Street').value;
    let ExpectedLease = document.getElementById('ExpectedLease').value;
    let ExpectedLeaseDuration = document.getElementById('ExpectedLeaseDuration').value;
    let Maintenance = document.getElementById('Maintenance').value;
    let Terms = document.getElementById('Terms').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;


        if(Length == "" || Width == "" || PlotArea == "" || Cent == "" ||
            Acre == "" || District == "" || Town == "" || Street == "" || ExpectedLease == "" || ExpectedLeaseDuration == "" || 
            Maintenance == "" || Terms == "" || PrimaryNumber == "" || SecondaryNumber == "")
        {
            alert("Please fill the Required fields");
        }
        else{
            $.ajax({
                url : 'land_lease_create/',
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
                    ExpectedLease : ExpectedLease,
                    ExpectedLeaseDuration : ExpectedLeaseDuration,
                    Maintenance : Maintenance,
                    Terms : Terms,
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
