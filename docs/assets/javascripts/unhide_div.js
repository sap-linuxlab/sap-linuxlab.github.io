function unhide_div(target, file) {
    var x = document.getElementById(target);
    if (x.style.display === "none") {
      x.style.display = "block";
      AsciinemaPlayer.create(file, document.getElementById(target));
    } else {
      x.style.display = "none";
    }
  } 
