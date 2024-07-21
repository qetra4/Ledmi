  jQuery(function($){
  $('#description p').each(function(i){
     $(this).attr('id', 'description-'+i);
  })
  });


  jQuery(function($){
  $('#button button').each(function(i){
     $(this).attr('id', 'button-'+i);
  })
  });


function toggle_visibility(button_id) {
   var the_num = button_id.replace(/^\D+/g, '');
   var description_id = 'description-' + the_num;
   var d = document.getElementById(description_id);
   var b = document.getElementById(button_id);
   if (d.style.display == 'block') {
      d.style.display = 'none';
      b.innerHTML = 'Show description';
   }
   else {
      d.style.display = 'block';
      b.innerHTML = 'Hide description';
   }
}
