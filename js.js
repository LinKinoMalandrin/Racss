window.onscroll = function() { inspectScrollable(); };

function useModal(id) {
	let modal = document.getElementById(id);
	modal.classList.add('open');

	window.onclick = function(event) {
		if (event.target == modal) {
			modal.classList.remove('open');
		}
	}
}

function toggle(id) {
	let doc = document.getElementById(id);
	if (doc.classList.contains('open')) {
		doc.classList.remove('open');
	} else {
		doc.classList.add('open');
	}
}

function toggleThis(doc) {
	if (doc.classList.contains('open')) {
		doc.classList.remove('open');
	} else {
		doc.classList.add('open');
	}
}

function closeModalParent(button) {
	let parent = button;
	while (parent = parent.parentNode) {
		if (parent.classList.contains('modal')) {
			parent.classList.remove('open');
			break;
		}
	}
}

function useAccordeon(id) {
	let accordeon = document.getElementById(id);
	if (accordeon.classList.contains('open')) {
		accordeon.classList.remove('open');
	} else {
		accordeon.classList.add('open');
	}
}

let modals = document.getElementsByClassName('modal');
setTimeout(
	function() {
		for (let m of modals) {
			m.style.visibility = "visible";
		}
	}, 1000);

function inspectScrollable() {
	if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
		for (let e of document.getElementsByClassName("onscroll")) e.classList.add('scroll');
	} else {
		for (let e of document.getElementsByClassName("onscroll")) e.classList.remove('scroll');
	}
}