$( document ).ready(function() {
  $( ".landmark1" ).keypress(function(e) {
    var key = e.keyCode;
    if (key >= 48 && key <= 57) {
        e.preventDefault();
    }
  });
  $( "#tags" ).keypress(function(e) {
    var key = e.keyCode;
    if (key >= 48 && key <= 57) {
        e.preventDefault();
    }
  });
});
//=========================multiple=====================================================================================
$(document).ready(function(){
   $('#multiple').multiselect({
      columns: 1,
      placeholder: 'SELECT 1 OR MORE AMENITIES'
   });
});
//=========================images=======================================================================================

const MAX_WIDTH = 320;
const MAX_HEIGHT = 180;
const MIME_TYPE = "image/jpeg";
const QUALITY = 0.7;
        const input = document.getElementById("img-input");
        input.onchange = function (ev) {
            const file = ev.target.files[0]; // get the file
            const blobURL = URL.createObjectURL(file);
            const img = new Image();
            img.src = blobURL;
            img.onerror = function () {
                URL.revokeObjectURL(this.src)
                console.log("Cannot load image");
            };
            img.onload = function () {
                URL.revokeObjectURL(this.src);
                const [newWidth, newHeight] = calculateSize(img, MAX_WIDTH, MAX_HEIGHT);
                const canvas = document.createElement("canvas");
                canvas.width = newWidth;
                canvas.height = newHeight;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(img, 0, 0, newWidth, newHeight);
                document.getElementById("root").append(canvas);
            };
        };
        function calculateSize(img, maxWidth, maxHeight) {
            let width = img.width;
            let height = img.height;
            if (width > height) {
                if (width > maxWidth) {
                    height = Math.round((height * maxWidth) / width);
                    width = maxWidth;
                }
            } else {
                if (height > maxHeight) {
                    width = Math.round((width * maxHeight) / height);
                    height = maxHeight;
                }
            }
            return [width, height];
        }
        function displayInfo(label, file) {
            const p = document.createElement('p');
            p.innerText = `${label} - ${readableBytes(file.size)}`;
            document.getElementById('root').append(p);
        }
        function readableBytes(bytes) {
            const i = Math.floor(Math.log(bytes) / Math.log(1024)),
                sizes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
            return (bytes / Math.pow(1024, i)).toFixed(2) + ' ' + sizes[i];
        }
//==========================amount======================================================================================
function onlyNumbers(evt) {
        var e = event || evt; // For trans-browser compatibility
        var charCode = e.which || e.keyCode;
            if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
        return true;
     }
     function NumToWord(inputNumber, outputControl) {
        var str = new String(inputNumber)
        var splt = str.split("");
        var rev = splt.reverse();
        var once = ['Zero', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine'];
        var twos = ['Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen'];
        var tens = ['', 'Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety'];
        numLength = rev.length;
        var word = new Array();
        var j = 0;
        for (i = 0; i < numLength; i++) {
            switch (i) {
            case 0:
            if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                 word[j] = '';
            }
            else {
                 word[j] = '' + once[rev[i]];
            }
                 word[j] = word[j];
        break;
            case 1:
            aboveTens();
        break;
            case 2:
                if (rev[i] == 0) {
                    word[j] = '';
                }
                else if ((rev[i - 1] == 0) || (rev[i - 2] == 0)) {
                    word[j] = once[rev[i]] + " Hundred ";
                }
                else {
                    word[j] = once[rev[i]] + " Hundred and";
                }
        break;
            case 3:
                if (rev[i] == 0 || rev[i + 1] == 1) {
                    word[j] = '';
                }
                else {
                    word[j] = once[rev[i]];
                }
                if ((rev[i + 1] != 0) || (rev[i] > 0)) {
                    word[j] = word[j] + " Thousand";
                }
        break;
            case 4:
                aboveTens();
        break;
            case 5:
                    if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                        word[j] = '';
                    }
                    else {
                        word[j] = once[rev[i]];
                    }
                    if (rev[i + 1] !== '0' || rev[i] > '0') {
                        word[j] = word[j] + " Lakh";
                    }
        break;
            case 6:
                    aboveTens();
        break;
            case 7:
                if ((rev[i] == 0) || (rev[i + 1] == 1)) {
                    word[j] = '';
                }
                else {
                    word[j] = once[rev[i]];
                }
                if (rev[i + 1] !== '0' || rev[i] > '0') {
                    word[j] = word[j] + " Crore";
                }
        break;
            case 8:
                aboveTens();
        break;
    default: break;
    }
    j++;
}
    function aboveTens() {
        if (rev[i] == 0) { word[j] = ''; }
        else if (rev[i] == 1) { word[j] = twos[rev[i - 1]]; }
        else { word[j] = tens[rev[i]]; }
    }
    word.reverse();
    var finalOutput = '';
    for (i = 0; i < numLength; i++) {
        finalOutput = finalOutput + word[i];
    }
    document.getElementById(outputControl).innerHTML = finalOutput;
    }

//==============================location======================================================================================
$(function() {
  var availableTags = ["Airoli East", "Airoli West ", "Ambernath East", "Ambernath West", "Ambivali", "Andheri East","Andheri West",
          "Apta", "Asangaon", "Atgaon", "Badlapur East", "Badlapur West", "Bamandongri", "Bandra East","Bandra West",
          "Belapur West", "Bhandup East", "Bhandup West", "Bhayander", "Bhivpuri Road", "Bhiwandi","Boisar West", "Borivali East",
          "Borivali West", "Byculla East", "Byculla West", "CSMT", "Charni East", "Charni West", "Chembur",
          "Chinchpokli", "Chunabhatti", "Churchgate East", "Churchgate West", "Cotton Green","Curry Road East", "Curry Road West",
          "Dadar East", "Dadar West", "Dahanu Road", "Dahisar East", "Dahisar West", "Dativali","Diva JN East", "Diva JN West", "Dockyard", "Dolavli",
          "Dombivli East", "Dombivali West", "Dronagiri", "Elphistone Road East", "Elphistone Road West","GTB Nagar", "Ghansoli",
          "Ghatkopar East", "Ghatkopar West", "Goregaon East", "Goregaon West", "Govandi East","Govandi West", "Grant Road East", "Grant Road West", "Hamrapur",
          "Jite", "Jogeshwari East", "Jogeshwari West", "Juchandra Road", "Juinagar East", "Juinagar West","Kalamboli", "Kalva East", "Kalva West",
          "Kalyan East", "Kalyan West", "Kaman Road", "Kamothe", "Kandivali East", "Kandivali West","Kanjur Marg East", "Kanjur Marg West", "Karjat",
          "Kasara", "Kasu", "Kelavli", "Kelva Road", "Khadavli", "Khandeshwar", "Khar East", "Khar West","Kharbao", "Khardi", "Kharghar", "Kharkopar",
          "Khopoli", "Kings Circle", "Kopar East", "Kopar West", "Koparkhairne", "Kurla East", "Kurla West","Lower Parel East", "Lower Parel West",
          "Lowjee", "Mahalakshmi East", "Mahalakshmi West", "Mahim JN East", "Mahim JN West", "Malad East","Malad West", "Mansarovar", "Mankhurd East",
          "Mankhurd West", "Marine Lines East", "Marin Lines West", "Masjid Bunder", "Matunga East","Matunga West", "Matunga Road East",
          "Matunga Road West", "Mira Road East", "Mira Road West", "Mulund", "Mumbai Central East","Mumbai Central West", "Mumbra East", "Mumbra West", "Nahur East",
          "Nahur West", "Naigaon East", "Naigaon West", "NallaSopara East", "NallaSopara West","Nariman Point", "Navade Road", "Navi Mumbai", "Neral",
          "Nerul", "Nidi", "Nilje", "Oshiwara", "Palasdhari", "Palghar", "Panvel East", "Panvel West","Parel East", "Parel West", "Pen", "Powai", "Prabhadevi",
          "Rabale", "Ranjanpada", "Ram Mandir", "Rasayani", "Reay Road", "Roha", "Sagar Sangam","Sakinaka East", "Sakinaka West", "Sandhurst Road East",
          "Sandhurst Road West", "Sanpada", "SantaCruz East", "SantaCruz West", "Saphale", "Seawood Darave","Sewri", "Shahad", "Shelu", "Sion", "Somtane",
          "Taloja", "Thakurali East", "Thakurli West", "Thane East", "Thane West", "Thansit","Tilaknagar East", "Tilaknagar West", "Titwala", "Turbhe",
          "Ulhasnagar East", "Ulhasnagar West", "Umroli Road", "Umbermali", "Uran", "Vadala Road East","Vadala Road West", "Vaitarana", "Vangani",
          "Vangaon", "Vasai Road East", "Vasai Road West", "Vashi East", "Vashi West", "Vasind","VidyaVihar East", "VidyaVihar West", "Vikhroli",
          "Vile Parle East", "Vile Parle West", "Virar East", "Virar West", "Vithalwadi East","Vithalwadi West", "Wadala"
    ];
  $("#tags").autocomplete({
    source: availableTags
  });
});
//======================================multiselect======================================================================


