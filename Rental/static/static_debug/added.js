
window.addEventListener("load",function(){

  jQuery(function($){
  $('#p_add p').each(function(i){
     $(this).attr('id', 'p_add-'+i);
  })
  });


  jQuery(function($){
  $('#input input').each(function(i){
     $(this).attr('id', 'input-'+i);
  })
  });
  function add(input_id) {
   var the_num = input_id.replace(/^\D+/g, '');
   var p_add_id = 'p_add-' + the_num;
   var d = document.getElementById(p_add_id);
   d.style.display = 'block';
   }

    // cod cod cod
});
