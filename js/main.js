/*
 *  Mobile Navagation Script
 */
let mainNav       = document.getElementById('main-nav')
let burgerButton  = document.getElementById('navbar-icon')

/*
 *  Burger Button Function
 */
function toggleMenu() {
  burgerButton.classList.toggle("navbar-open");
  mainNav.classList.toggle("menu-open")
}

/*
 *  Event Listener
 */

burgerButton.addEventListener("click", toggleMenu);