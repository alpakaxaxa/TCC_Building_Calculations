function createUUID() {
  let dt = new Date().getTime();
  let uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
    let r = (dt + Math.random() * 16) % 16 | 0;
    dt = Math.floor(dt / 16);
    return (c == 'x' ? r : (r & 0x3 | 0x8)).toString(16);
  });
  return uuid;
}

window.onload = function () {
  const form = document.getElementById('buildingInformationForm');
  form.addEventListener('submit', validateBuildingInformationForm);
};

function validateBuildingInformationForm() {
  let el = document.getElementById('uID');
  let uID = createUUID();
  el.value = uID
  let l = localStorage.length
  localStorage.setItem((l+1).toString(), uID)
  return true;
}