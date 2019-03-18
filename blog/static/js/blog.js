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
	var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
       slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active-dot", "");
    }	
    slides[slideIndex-1].style.display = "block";
	dots[slideIndex-1].className += " active-dot";
    setTimeout(showSlides, 5000); // Change image every 2 seconds
}

window.onscroll = function() {scrollFunc()};
var header = document.getElementById("navbar");
var sticky = header.offsetTop;
function scrollFunc() {
	if (window.pageYOffset > sticky) {
		header.classList.add("sticky");
	} else {
		header.classList.remove("sticky");
	}
}

var image1 = document.querySelector(".img1");
var image2 = document.querySelector(".img2");
var image3 = document.querySelector(".img3");
function setTranslate(xPos, yPos, el) {
	el.style.transform = "translate3d(" + xPos + ", " + yPos + "px, 0)";
}
window.addEventListener("DOMContentLoaded", scrollLoop, false);
var xScrollPosition;
var yScrollPosition;

function scrollLoop() {
	xScrollPosition = window.scrollX;
	yScrollPosition = window.scrollY;
	setTranslate(0, yScrollPosition / -3, image1);
	setTranslate(0, yScrollPosition / -3, image2);
	setTranslate(0, yScrollPosition / -3, image3);
	requestAnimationFrame(scrollLoop);
}