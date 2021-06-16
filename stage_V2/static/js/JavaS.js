function openNav() {
  document.getElementById("mySidebar").style.width = "160px";
  document.getElementById("main").style.marginLeft = "-200px";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  document.getElementById("sidebarModelisme").style.width = "0";
  document.getElementById("sidebarPhilatelie").style.width = "0";
  document.getElementById("sidebarOenoligie").style.width = "0";
  document.getElementById("sidebarAutres").style.width = "0";
}

function openNavmodelisme() {
  closeNav()
  openNav()
  document.getElementById("sidebarModelisme").style.width = "160px";
}

function openNavphilatelie() {
  closeNav()
  openNav()
  document.getElementById("sidebarPhilatelie").style.width = "160px";
}

function openNavoenologie() {
  closeNav()
  openNav()
  document.getElementById("sidebarOenoligie").style.width = "160px";
}

function openNavautres() {
  closeNav()
  openNav()
  document.getElementById("sidebarAutres").style.width = "160px";
}


function changecolor() {
  document.body.classList.toggle("dark-mode");
  if (document.getElementById('ajouterblack')) {

      if (document.getElementById('ajouterblack').style.display == 'none') {
          document.getElementById('ajouterblack').style.display = 'block';
          document.getElementById('ajouterwhite').style.display = 'none';
      }
      else {
          document.getElementById('ajouterblack').style.display = 'none';
          document.getElementById('ajouterwhite').style.display = 'block';
      }
  }
  document.getElementsById('annonceShort').classList.toggle("dark-mode");
}


let rotateAngle = 180;
function rotate() {
  image = document.getElementById('logobw');
  image.setAttribute("style", "transform: rotate(" + rotateAngle + "deg)");
  rotateAngle = rotateAngle + 180;
}

var loadFile = function(event) {
  var output = document.getElementById('output');
  output.src = URL.createObjectURL(event.target.files[0]);
  output.onload = function() {
  URL.revokeObjectURL(output.src)
  }
};

function close_select(){
  document.getElementById("profil_avion").style.display = "none";
  document.getElementById("profil_timbre").style.display = "none";
  document.getElementById("profil_vins").style.display = "none";
  document.getElementById("profil_autre").style.display = "none";
}

function selectavion() {
  close_select()
  document.getElementById("profil_avion").style.display = "block";
}

function selecttimbre() {
  close_select()
  document.getElementById("profil_timbre").style.display = "block";
}

function selectvins() {
  close_select()
  document.getElementById("profil_vins").style.display = "block";
}

function selectautre() {
  close_select()
  document.getElementById("profil_autre").style.display = "block";
}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}

function MdP() {
  var x = document.getElementById("mymdp");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}

function openedit() {
  document.getElementById("editchoix").style.display = "inline-flex";
  document.getElementById("closebuttonedit").style.display = "block";
}

function clsedit() {
  document.getElementById("editchoix").style.display = "none";
  document.getElementById("closebuttonedit").style.display = "none";
}