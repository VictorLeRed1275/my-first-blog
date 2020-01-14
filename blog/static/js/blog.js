//Loader
function onReady(callback) {
	var intervalId = window.setInterval(function() {
		if (document.getElementsByTagName('body')[0] !== undefined) {
			window.clearInterval(intervalId);
			callback.call(this);
		}
	}, 1000);
}

function setVisible(selector, visible) {
	document.querySelector(selector).style.display = visible ? 'block' : 'none';
}

onReady(function() {
	setVisible('body', true);
	setVisible('.load-container', false);
});

//Slideshow
var slideIndex = 0;
showSlides();

function showSlides() {
    var i;
    var slides = document.getElementsByClassName("slide");
	var slide_center = document.getElementsByClassName("slide-center");
	var dots = document.getElementsByClassName("dot");
    for (i = 0; i < slides.length; i++) {
		slides[i].style.opacity = "0";
		slide_center[i].style.opacity = "0";
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(" active-dot", "");
    }
	slides[slideIndex-1].style.opacity = "1";
	slide_center[slideIndex-1].style.opacity = "1";
	dots[slideIndex-1].className += " active-dot";
    setTimeout(showSlides, 5000);
}

var slideIndex = 1;
showDivs(slideIndex);

function currentDiv(n) {
	showDivs(slideIndex = n);
}

function showDivs(n) {
	var i;
	var x = document.getElementsByClassName("slide");
	var slide_center = document.getElementsByClassName("slide-center");
	var dots = document.getElementsByClassName("dot");
	if (n > x.length) {slideIndex = 1}
	if (n < 1) {slideIndex = x.length}
	for (i = 0; i < x.length; i++) {
		x[i].style.opacity = "0";
		slide_center[i].style.opacity = "0";
	}
	for (i = 0; i < dots.length; i++) {
		dots[i].className = dots[i].className.replace(" active-dot", "");
	}
	x[slideIndex-1].style.opacity = "1";
	slide_center[slideIndex-1].style.opacity = "1";
	dots[slideIndex-1].className += " active-dot";
}

var clickdots = document.getElementsByClassName("dot");
clickdots[0].onclick = function(){
	currentDiv(1);
}
clickdots[1].onclick = function(){
	currentDiv(2);
}
clickdots[2].onclick = function(){
	currentDiv(3);
}

//Animation
window.onscroll = function() {scrollFunc()};
var header = document.getElementById("navbar");
var sticky = header.offsetTop;
function scrollFunc() {
	if (window.pageYOffset > sticky) {
		header.classList.add("sticky");
		document.getElementById("top-scroll").style.display = "block";
	} else {
		header.classList.remove("sticky");
		document.getElementById("top-scroll").style.display = "none";
	}
	if (window.pageYOffset > 830) {
		document.getElementsByClassName("skill-one")[0].style.width = "90%";
		document.getElementsByClassName("skill-two")[0].style.width = "80%";
		document.getElementsByClassName("skill-three")[0].style.width = "65%";
		document.getElementsByClassName("skill-four")[0].style.width = "60%";
		document.getElementsByClassName("skill")[0].style.opacity = "1";
		document.getElementsByClassName("skill")[1].style.opacity = "1";
		document.getElementsByClassName("skill")[2].style.opacity = "1";
		document.getElementsByClassName("skill")[3].style.opacity = "1";
	}
	if (window.pageYOffset > 260) {
		document.getElementsByClassName("about-photo")[0].style.opacity = "1";
	}
	if (window.pageYOffset == 0) {
		document.getElementsByClassName("about-photo")[0].style.opacity = "0";
		document.getElementsByClassName("skill-one")[0].style.width = "0%";
		document.getElementsByClassName("skill-two")[0].style.width = "0%";
		document.getElementsByClassName("skill-three")[0].style.width = "0%";
		document.getElementsByClassName("skill-four")[0].style.width = "0%";
		document.getElementsByClassName("skill")[0].style.opacity = "0";
		document.getElementsByClassName("skill")[1].style.opacity = "0";
		document.getElementsByClassName("skill")[2].style.opacity = "0";
		document.getElementsByClassName("skill")[3].style.opacity = "0";
	}
}

//Parallax
if ($(window).width() > 700) {
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
		setTranslate(0, yScrollPosition / +3, image1);
		setTranslate(0, yScrollPosition / +3, image2);
		setTranslate(0, yScrollPosition / +3, image3);
		requestAnimationFrame(scrollLoop);
	}
}

//Scroll to top
$(function() {
	$('#top-scroll').bind('click', function(event) {
		$("html, body").animate({ scrollTop: 0 }, 1000);
		event.preventDefault();
	});
});

//Modal
var modal = document.getElementById('myModal');
var span = document.getElementsByClassName("modal-close")[0];
span.onclick = function() {
	modal.style.display = "none";
}
window.onclick = function(event) {
	if (event.target == modal) {
		modal.style.display = "none";
	}
}

//Counter
$(window).scroll(startCounter);
function startCounter() {
	if ($(window).scrollTop() > 1150 && $(window).scrollTop() < 1160) {
		$(window).off("scroll", startCounter);
		$('.amount').each(function () {
			var $this = $(this);
			jQuery({ Counter: 0 }).animate({ Counter: $this.attr("data") }, {
				duration: 1000,
				easing: 'swing',
				step: function () {
					$this.text(Math.ceil(this.Counter));
				}
			});
		});
	}
}

//Mini-bar
var menu_bars = document.getElementsByClassName("menu-bars")[0];
menu_bars.onclick = function(){
	var toggle = menu_bars.classList.toggle("change");
	if(toggle){
		document.getElementsByClassName("main-menu")[0].style.display = "block";
	} else {
		document.getElementsByClassName("main-menu")[0].style.display = "none";
	}
}

var dropbtn = document.getElementsByClassName("dropbtn")[0];
dropbtn.onclick = function() {
	document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function(event) {
	if (!event.target.matches('.dropbtn')) {
	  	var dropdowns = document.getElementsByClassName("dropdown-content");
	  	var i;
	  	for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
		  		openDropdown.classList.remove('show');
			}
	  	}
	}
}