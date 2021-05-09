// Events
window.addEventListener("load", checkQueryString);
window.addEventListener("load", resetStorage);
document.addEventListener("change", function (e) {
    if (e.target.className == "input") {
        localStorage.setItem(e.target.name, e.target.value);
    }
})

// Check if uID query parameter is given. If uID is specified, 
// form fields should be populated by flask and not javascript
// else display local storage data
function checkQueryString() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const uID = urlParams.get('uID');
    if (!uID) {
        populateFormWithLocalStorage();
    }
}

// Prepopulate the form with local storage data so that user already has a working blueprint for his record
function populateFormWithLocalStorage() {
    let elems = document.getElementsByClassName("input");
    for (let i = 0; i < elems.length; i++) {
        elems[i].value = localStorage.getItem(elems[i].name);
    }
}

/* // Function to reset local storage upon form submission
function resetStorage() {
    // TODO Usertests are needed in order to evaluate if reset of local storage is needed
    const form = document.getElementById('buildingInformationForm');
    form.addEventListener('submit', function() {
        // Return true to execute form submission
        return true
    }); 
} */
