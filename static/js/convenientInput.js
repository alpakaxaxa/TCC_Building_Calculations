window.addEventListener("load", checkQueryString);
window.addEventListener("load", resetStorage)
// Check if uID query parameter is given. If uID is specified, 
// form fields should be populated by flask and not javascript
function checkQueryString() {
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);
    const uID = urlParams.get('uID');
    if (!uID) {
        populateFormWithLocalStorage()
    }
}

document.addEventListener('change', function (e) {
    if (e.target.className == "input") {
        localStorage.setItem(e.target.name, e.target.value);
    }
})

function populateFormWithLocalStorage() {
    let elems = document.getElementsByClassName("input");
    for (i = 0; i < elems.length; i++) {
        elems[i].value = localStorage.getItem(elems[i].name);
    }
}

function resetStorage() {
    const form = document.getElementById('buildingInformationForm');
    form.addEventListener('submit', function() {
        localStorage.clear();
        // Return true to execute form submission
        alert("Local storage has been cleared")
        return true
    });
}