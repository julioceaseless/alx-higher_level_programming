/* select the element */
const element = document.querySelector('header');
/* if element selected, set color */
if (element) {
  element.style.color = '#FF0000';
} else {
  console.error('Header element not found');
}
