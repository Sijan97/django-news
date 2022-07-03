'use strict';

let nav = document.querySelector('.navbar');
let navStick = nav.offsetTop;

window.onscroll = function () {
    if (window.scrollY > navStick) {
        nav.classList.add('sticky');
    } else {
        nav.classList.remove('sticky');
    }
}