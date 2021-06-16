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
} 

let rotateAngle = 180;
function rotate() {
  image = document.getElementById('logobw');
  image.setAttribute("style", "transform: rotate(" + rotateAngle + "deg)");
  rotateAngle = rotateAngle + 180;
}