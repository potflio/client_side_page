


function Calculate() {
    //For House
var HouseLength = parseFloat(document.getElementById('HouseLength').value) || 0;
var HouseWidth = parseFloat(document.getElementById('HouseWidth').value) || 0;

var HousePlotArea = HouseLength * HouseWidth;
var HouseCent = HousePlotArea / 436;

document.getElementById('HousePlotArea').value = HousePlotArea.toFixed(2);
document.getElementById('HouseCent').value = HouseCent.toFixed(2);
    //For Land
var LandLength = parseFloat(document.getElementById('LandLength').value) || 0;
var LandWidth = parseFloat(document.getElementById('LandWidth').value) || 0;

var LandPlotArea = LandLength * LandWidth;
var LandCent = LandPlotArea / 436;

document.getElementById('LandPlotArea').value = LandPlotArea.toFixed(2);
document.getElementById('LandCent').value = LandCent.toFixed(2);
}

function residential_resale_create(){
    let BhkType = document.getElementById('BhkType').value;
    let TotalFloor = document.getElementById('TotalFloor').value;
    let PropertyAge = document.getElementById('PropertyAge').value;
    let HouseLength = document.getElementById('HouseLength').value;
    let HouseWidth = document.getElementById('HouseWidth').value;
    let HousePlotArea = document.getElementById('HousePlotArea').value;
    let HouseCent = document.getElementById('HouseCent').value;
    let LandLength = document.getElementById('LandLength').value;
    let LandWidth = document.getElementById('LandWidth').value;
    let LandPlotArea = document.getElementById('LandPlotArea').value;
    let LandCent = document.getElementById('LandCent').value;
    let Parking = document.getElementById('Parking').value;
    let Terrace = document.getElementById('Terrace').value;
    let Hall = document.getElementById('Hall').value;
    let Bedroom = document.getElementById('Bedroom').value;
    let Bathroom = document.getElementById('Bathroom').value;
    let District = document.getElementById('District').value;
    let Town = document.getElementById('Town').value;
    let Street = document.getElementById('Street').value;
    let ExpectedPrice = document.getElementById('ExpectedPrice').value;
    let Description = document.getElementById('Description').value;
    let PrimaryNumber = document.getElementById('PrimaryNumber').value;
    let SecondaryNumber = document.getElementById('SecondaryNumber').value;

        if(BhkType == "" || TotalFloor == "" || PropertyAge == "" || HouseLength == "" || HouseWidth == "" || LandLength == "" || LandWidth == "" || 
        Parking == "" || Terrace == "" || Hall == "" || Bedroom == "" || Bathroom == "" || District == "" || Town == "" || Street == "" || ExpectedPrice == "" ||
        Description == "" || PrimaryNumber == "" || SecondaryNumber == ""){
            alert("Please fill the Required Field🥺")
        }
        else{
        $.ajax({
            url : 'residential_resale_create/',
            type : 'POST',
            data : {
            BhkType : BhkType,
            TotalFloor : TotalFloor,
            PropertyAge : PropertyAge,
            HouseLength : HouseLength,
            HouseWidth : HouseWidth,
            HousePlotArea : HousePlotArea,
            HouseCent : HouseCent,
            LandLength : LandLength,
            LandWidth : LandWidth,
            LandPlotArea : LandPlotArea,
            LandCent : LandCent,
            Parking : Parking,
            Terrace : Terrace,
            Hall : Hall,
            Bedroom : Bedroom,
            Bathroom : Bathroom,
            District : District,
            Town : Town,
            Street : Street,
            ExpectedPrice : ExpectedPrice,
            Description : Description,
            PrimaryNumber : PrimaryNumber,
            SecondaryNumber : SecondaryNumber,
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(){
            alert("Your Property Posted Successfully😊");
        },
        error:function(){
            alert("Sorry Some Error Occurs😖");
        }
        });
    }

}