let Btn = document.getElementById('btn');
let Nav = document.querySelector('.dropdown-content');

Btn.addEventListener('click', function(){
  Btn.classList.toggle('active');
  Nav.style.display = 'block';
})

jQuery(function($){
	$(document).mouseup( function(e){ //
		var div = $( ".dropdown-content" );
		if ( !div.is(e.target)
		    && div.has(e.target).length === 0 ) {
			div.hide();
		}
	});
});

