#!/usr/bin/node
/*
 * Javascript updates the text color of the header
 * element to red (#FF0000). Does not use JQuery API
 */

/* check if DOM is ready */
document.addEventListener('DOMContentLoaded', () => {
  /* select element */
  const headerElement = document.querySelector('header');

  /* modify element if selected */
  if (headerElement) {
    headerElement.style.color = '#FF0000';
  } else {
    console.error('Header element not found');
  }
});
