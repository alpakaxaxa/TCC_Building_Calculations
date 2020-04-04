window.addEventListener("load", checkQueryString);

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
    for (i=0;i<elems.length;i++) {
        elems[i].value = localStorage.getItem(elems[i].name);
    }
}