function unhide_div(target, file) {
    var x = document.getElementById(target);
    if (x.style.display === "none") {
      x.style.display = "inline";
      AsciinemaPlayer.create(file, document.getElementById(target),
      {fit: "none"}
    );
    } else {
      x.style.display = "none";
      document.getElementById(target).getElementsByClassName('ap-wrapper')[0].remove()
    }
  } 
