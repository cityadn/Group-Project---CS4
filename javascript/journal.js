function _(id){
  return document.getElementById(id);
}

function getRs() {
  let txt = _('txt').value;
  const d = new Date();

  _('rs').innerHTML += `<div class="card"><p>${txt}</p>
   <small>${d.toLocaleTimeString()}, ${d.toLocaleDateString()}</small></div>`
}

/* Reference: Javascript tutorial = https://www.w3schools.com/js/DEFAULT.asp */
