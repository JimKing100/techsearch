const preResultsContainer = document.querySelector('.pre-results-container')
// const logoImage = document.querySelector('.image')
const resultsContainer = document.querySelector('.results-container')


console.log(window.location)
if (window.location.href.includes("output")) {
  // console.log('output page')
  // logoImage.style.display = "none"
  preResultsContainer.style.display = "none"
  resultsContainer.style.height = "auto"
}
