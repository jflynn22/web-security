function startTimer(timer){ 
  seconds = parseInt(timer) || 3;
  setTimeout(function() { 
    window.confirm("Time is up!");
    window.history.back();
  }, seconds * 1000);
}

$(document).ready(function() {
  let timer = $('[name="timerdata"]').attr("content")
  timer = timer.substring(0, timer.length-1)
  console.log(timer)
    $("#image").load("startTimer('{{ timer }}');")
  })