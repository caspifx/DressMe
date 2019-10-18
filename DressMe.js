var options = {}

// JavaScript source code
document.addEventListener('DOMContentLoaded', function () {
    var elems = document.querySelectorAll('.slider');
    var instances = M.Slider.init(elems, options);
});
$(document).ready(function () {
    $('select').formSelect();
});
function loadOutfit(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

        if(this.responseText != 'No Outfit') {
            var txt = this.responseText.split('Pant');
            var top = txt[0];
            var pants = "Pant" + txt[1];
        } else {
            top = this.responseText;
        }
       var upper = document.getElementById("demo");
       upper.innerHTML = top;
       var lower = document.getElementById("demo2");
       lower.innerHTML = pants;
       upper.style.color =  "#"  + top.split("#")[1];
       console.log("#"  + top.split("#")[1]);
       lower.style.color =  "#"  + pants.split("#")[1];
      }
    };
  xhttp.open("GET", "/gen-outfit", true);
  xhttp.send();
}