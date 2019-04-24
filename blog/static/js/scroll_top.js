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

//Scroll to top
$(function() {
	$('#top-scroll').bind('click', function(event) {
		$("html, body").animate({ scrollTop: 0 }, 1000);
		event.preventDefault();
	});
});
	
//Sticky nav-bar
window.onscroll = function() {scrollFunc()};
var header = document.getElementById("navbar");
var sticky = header.offsetTop;
function scrollFunc() {
	if (window.pageYOffset > sticky) {
		document.getElementById("top-scroll").style.display = "block";
	} else {
		document.getElementById("top-scroll").style.display = "none";
	}
}

//Mini-menu toggle
var menu_bars = document.getElementsByClassName("menu-bars")[0];
menu_bars.onclick = function(){
	var toggle = menu_bars.classList.toggle("change");
	if(toggle){
		document.getElementsByClassName("main-menu")[0].style.display = "block";
	} else {
		document.getElementsByClassName("main-menu")[0].style.display = "none";
	}
}

var image1 = document.querySelector(".img1");
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
	if(image1 != undefined){
		setTranslate(0, yScrollPosition / -3, image1);
	}
	if(image3 != undefined){
		setTranslate(0, yScrollPosition / -3, image3);
	}
	requestAnimationFrame(scrollLoop);
}