$(document).ready(function(){

	var N
	var note_arr = []
	var list_arr = []
	var value = ''
	N = 0

	$('#add_list').click(function(){
		$('#list').append('<input type="checkbox"><label><input id="num'+ String(N) +'" class="list_fragments" type="text"></label><br>')
		N++
	});

	$("#done_list").click(function() {
    var value = ''
		for (var i = 0; i <= N-1; i++) {
			if ($('#num' + String(i)).is(':checked')){
				value += 'done=1' + $('#num' + String(i)).val() + '%%_next_%%'
			}else{
				value += 'done=0' + $('#num' + String(i)).val() + '%%_next_%%'
			}
		}
    $('#list_input').val(
			value
		)
  });

  $('li.note').click(function(){
  	$(this).toggleClass('active_note')
  });

  $('li.list').click(function(){
  	$(this).toggleClass('active_list')
  });

  $('#submit').click(function(){
  	$('.active_note').each(function(){
  		note_arr.push($(this).val())
  	})
  	for (var i = 0; i < note_arr.length; i++) {
  		value += (String(note_arr[i]) + ' ')
  	}
  	$('#note_id').val(value)

  	value = ''

  	$('.active_list').each(function(){
  		list_arr.push($(this).val())
  	})
  	for (var i = 0; i < list_arr.length; i++) {
  		value += (String(list_arr[i]) + ' ')
  	}
  	$('#list_id').val(value)
  });

});