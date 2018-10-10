var user = document.getElementById('user');
var top_menu = document.getElementById("top-menu");
var logonDisplay = false;
user.onclick = function() {
	if (logonDisplay == false) {
		top_menu.style.display = "block";
		logonDisplay = true;
	} else if (logonDisplay == true) {
		top_menu.style.display = "none";
		logonDisplay = false;
	}
}

var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 5000); // Change image every 2 seconds
}

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function stickynavbar() {
	if (window.pageYOffset >= sticky) {
		navbar.classList.add("sticky")
	} else {
		navbar.classList.remove("sticky");
	}
}
window.onscroll = function() {stickynavbar()};

var image1 = document.querySelector(".img1");
var image2 = document.querySelector(".img2");
var image3 = document.querySelector(".img3");
var image4 = document.querySelector(".img4");
function setTranslate(xPos, yPos, el) {
	el.style.transform = "translate3d(" + xPos + ", " + yPos + "px, 0)";
}
window.addEventListener("DOMContentLoaded", scrollLoop1, false);
var xScrollPosition;
var yScrollPosition;
xScrollPosition = window.scrollX;
yScrollPosition = window.scrollY;
function scrollLoop1() {
	setTranslate(0, yScrollPosition * -0.2, image1);
	setTranslate(0, yScrollPosition * -0.2, image2);
	setTranslate(0, yScrollPosition * -0.2, image3);
	requestAnimationFrame(scrollLoop1);
}