function prepare_vis(options) {

  var elem = document.getElementById('made-in-ny');
  elem.parentNode.removeChild(elem)
  var anchor = document.getElementById('anchor');

  var div_ = document.createElement('div');
  div_.setAttribute( "id", "made-in-ny" );
  anchor.appendChild(div_);

  if( window.innerWidth <= 700) {
    var video_height = document.querySelector('.other_img').offsetHeight;
    options.width = document.querySelector('.other_img').offsetWidth;
    document.getElementById('anchor').setAttribute("style","display:block;height:video_height");
    document.getElementById('anchor').style.height=video_height;
  }
  var video_height = window.innerHeight;
  if( window.innerWidth > 700) {
    options.width = window.innerWidth/2;
    document.getElementById('anchor').setAttribute("style","display:block;height:options.width");
    document.getElementById('anchor').style.height=video_height;
  }
  madeInNy = new Vimeo.Player('made-in-ny', options);
  document.querySelector('.footer_container').scrollIntoView({behavior: 'smooth',});
  madeInNy.play().then(function() {
  // the video was played
  document.querySelector('.footer_container').scrollIntoView({behavior: 'smooth',});
  }).catch(function(error) {
  switch (error.name) {
      case 'PasswordError':
          // the video is password-protected and the viewer needs to enter the
          // password first
          break;

      case 'PrivacyError':
          // the video is private
          break;

      default:
          // some other error occurred
          break;
  }
  });



}

function Ovision() {
    var options = {
        id: 711873567,
        width: 640,
        loop: true
    };
    prepare_vis(options);

}

function TVCPolice() {
    var options = {
        id: 833502653,
        width: 640,
        loop: true
    };
    prepare_vis(options);
}

function Yachtline() {
    var options = {
        id: 676594556,
        width: 640,
        loop: true
    };
    prepare_vis(options);
}

function MelScienceTonesOfBoxes() {
    var options = {
        id: 711873567,
        width: 640,
        loop: true
    };
    prepare_vis(options);
}

function BeautyOfChemistry() {
    var options = {
        id: 676596682,
        width: 640,
        loop: true
    };
    prepare_vis(options);
}

function MelSciencePresent() {
    var options = {
        id: 679550535,
        width: 640,
        loop: true
    };
    prepare_vis(options);
}
