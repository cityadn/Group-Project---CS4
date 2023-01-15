/* Reference: Javascript tutorial = https://www.w3schools.com/js/DEFAULT.asp */
/* Reference: Javascript Math Function = https://www.w3schools.com/js/js_math.asp */
const startingMinutes = 10;
let time = startingMinutes * 60;

const countdownEl = document.getElementById('countdown');

setInterval(updateCountdown, 1000);

function updateCountdown() {
  const minutes = Math.floor(time/60);
  let seconds = time % 60;

  seconds = seconds < 10 ? '0' + seconds : seconds;

  countdownEl.innerHTML = `${minutes}: ${seconds}`;
  time--;
  time = time < 0 ? 0:time;
}
