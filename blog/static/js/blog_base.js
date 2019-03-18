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

var overlay_drop = document.getElementById("overlay-drop");
var dropbtn = document.getElementById("dropbtn");
var overdrop = false;
overlay_drop.onclick = function() {
	if (overdrop == false) {
		document.getElementById("overlay-dropdown").style.display = "block";
		overlay_drop.className = overlay_drop.className.replace(" glyphicon-chevron-down", " glyphicon-chevron-up");
		overdrop = true;
	} else {
		document.getElementById("overlay-dropdown").style.display = "none";
		overlay_drop.className = overlay_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
		overdrop = false;
	}
}

var post = document.getElementsByClassName("item-container");
var th = document.getElementsByClassName("th");
for (var i in th) {
	if (th[i].className == "th drop-active") {
		dropbtn.innerHTML = th[i].innerHTML;
	}
}

var the_large = document.getElementById("th-large");
var the_list = document.getElementById("th-list");
the_large.onclick = function() {
	the_large.className = "th drop-active";
	the_list.className = "th";
	for (var i in th) {
		if (th[i].className == "th drop-active") {
			dropbtn.innerHTML = th[i].innerHTML;
		}
	}
    for (i = 0; i < post.length; i++) {
        post[i].className = post[i].className.replace(" list-container", " box-container");
    }
	document.getElementById("overlay-dropdown").style.display = "none";
	overlay_drop.className = overlay_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
}

the_list.onclick = function() {
	the_list.className = "th drop-active";
	the_large.className = "th";
	for (var i in th) {
		if (th[i].className == "th drop-active") {
			dropbtn.innerHTML = th[i].innerHTML;
		}
	}
    for (i = 0; i < post.length; i++) {
        post[i].className = post[i].className.replace(" box-container", " list-container");
    }
	document.getElementById("overlay-dropdown").style.display = "none";
	overlay_drop.className = overlay_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
}

//////////

var select_drop = document.getElementById("select-drop");
var select_dropbtn = document.getElementById("select-dropbtn");
var seldrop = false;
select_drop.onclick = function() {
	if (seldrop == false) {
		document.getElementById("select").style.display = "block";
		select_drop.className = select_drop.className.replace(" glyphicon-chevron-down", " glyphicon-chevron-up");
		seldrop = true;

	} else {
		document.getElementById("select").style.display = "none";
		select_drop.className = select_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
		seldrop = false;

	}
}

var post = document.getElementsByClassName("item-container");
var sl = document.getElementsByClassName("sl");
for (var i in sl) {
	if (sl[i].className == "sl drop-active-select") {
		select_dropbtn.innerHTML = sl[i].innerHTML;
	}
}

var date = document.getElementById("date");
var title = document.getElementById("title");
var comment = document.getElementById("comment");

date.onclick = function() {
	date.className = "sl drop-active-select";
	title.className = "sl";
	comment.className = "sl";
	for (var i in sl) {
		if (sl[i].className == "sl drop-active-select") {
			select_dropbtn.innerHTML = sl[i].innerHTML;
		}
	}
	document.getElementById("select").style.display = "none";
	select_drop.className = select_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
	var list, i, switching, shouldSwitch;
	list = document.getElementById("sort");
	switching = true;
	while (switching) {
		switching = false;
		var c = list.getElementsByClassName("video");
		var b = list.getElementsByClassName("date-time");
		var a = list.getElementsByClassName("post");
		for (i = 0; i < (b.length - 1); i++) {
			shouldSwitch = false;
			if (Number(b[i].innerHTML) < Number(b[i + 1].innerHTML)) {
				shouldSwitch = true;
				break;
			}
		}
		if (shouldSwitch) {
			a[i].parentNode.insertBefore(a[i + 1], a[i]);
			switching = true;
		} else if (shouldSwitch && c != 'undefined') {
			c[i].parentNode.insertBefore(c[i + 1], c[i]);
			switching = true;
		}
	}
}

title.onclick = function() {
	title.className = "sl drop-active-select";
	comment.className = "sl";
	date.className = "sl";
	for (var i in sl) {
		if (sl[i].className == "sl drop-active-select") {
			select_dropbtn.innerHTML = sl[i].innerHTML;
		}
	}
	document.getElementById("select").style.display = "none";
	select_drop.className = select_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
	var list, i, switching, shouldSwitch;
	list = document.getElementById("sort");
	switching = true;
	while (switching) {
		switching = false;
		var c = list.getElementsByClassName("video");
		var b = list.getElementsByClassName("name");
		var a = list.getElementsByClassName("post");
		for (i = 0; i < (b.length - 1); i++) {
			shouldSwitch = false;
			if (b[i].innerHTML.toLowerCase() > b[i + 1].innerHTML.toLowerCase()) {
				shouldSwitch = true;
				break;
			}
		}
		if (shouldSwitch) {
			a[i].parentNode.insertBefore(a[i + 1], a[i]);
			switching = true;
		} else if (shouldSwitch && c != 'undefined') {
			c[i].parentNode.insertBefore(c[i + 1], c[i]);
			switching = true;
		}
	}
}

comment.onclick = function() {
	comment.className = "sl drop-active-select";
	title.className = "sl";
	date.className = "sl";
	for (var i in sl) {
		if (sl[i].className == "sl drop-active-select") {
			select_dropbtn.innerHTML = sl[i].innerHTML;
		}
	}
	document.getElementById("select").style.display = "none";
	select_drop.className = select_drop.className.replace(" glyphicon-chevron-up", " glyphicon-chevron-down");
	var list, i, switching, shouldSwitch;
	list = document.getElementById("sort");
	switching = true;
	while (switching) {
		switching = false;
		var c = list.getElementsByClassName("video");
		var b = list.getElementsByClassName("comment-sort");
		var a = list.getElementsByClassName("post");
		for (i = 0; i < (b.length - 1); i++) {
			shouldSwitch = false;
			if (Number(b[i].innerHTML) < Number(b[i + 1].innerHTML)) {
				shouldSwitch = true;
				break;
			}
		}
		if (shouldSwitch) {
			a[i].parentNode.insertBefore(a[i + 1], a[i]);
			switching = true;
		} else if (shouldSwitch && c != 'undefined') {
			c[i].parentNode.insertBefore(c[i + 1], c[i]);
			switching = true;
		}
	}
}