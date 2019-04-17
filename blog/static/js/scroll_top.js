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

$(function() {
	$('#top-scroll').bind('click', function(event) {
		$("html, body").animate({ scrollTop: 0 }, 1000);
		event.preventDefault();
	});
});
	
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

var menu_bars = document.getElementsByClassName("menu-bars")[0];
menu_bars.onclick = function(){
	var toggle = menu_bars.classList.toggle("change");
	if(toggle){
		document.getElementsByClassName("main-menu")[0].style.display = "block";
	} else {
		document.getElementsByClassName("main-menu")[0].style.display = "none";
	}
}