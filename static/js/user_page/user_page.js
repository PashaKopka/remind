$(document).ready(function(){

	var note_arr = []
	var note_num
	var old_text
	var number
	var difference
	var start = 1

	$('.note').each(function(){
  	note_arr.push($(this))
  })

  note_num = note_arr.length

  if (note_num / 5 < 3) {
	  $('.note_grid').css('grid-template-rows', 'auto '.repeat(3));
  }else{
	  $('.note_grid').css('grid-template-rows', 'auto '.repeat(note_num / 5 + 2));
  }

  for (var i = 0; i < note_num; i++) {
		if (i != 0 && (i % 5) == 0) {
			start++
		}
		number = (start - 2) * 5 + (i % 5)

		if (number >= 0 && (note_arr[number].css('grid-row').substr(4) >= (start + 1))) {
			difference = note_arr[number].css('grid-row').substr(4) - (start + 1)

				if (note_arr[i].find('p').html().length <= 100) {
					$(note_arr[i]).css('grid-row', ((difference + start + 1) + ' / ' + (difference + start + 2)));
				}else if(note_arr[i].html().length > 100 && (note_arr[i].html()).length <= 200){
					$(note_arr[i]).css('grid-row', ((difference + start + 1) + ' / ' + (difference + start + 3)));
					$(note_arr[i]).css('min-height', '300px')
				}else{
					$(note_arr[i]).css('grid-row', ((difference + start + 1) + ' / ' + (difference + start + 3)));
					$(note_arr[i]).css('min-height', '300px')
				}

		}else{
	  	if (note_arr[i].find('p').html().length <= 150) {
				$(note_arr[i]).css('grid-row', (start + ' / ' + (start + 1)));
			}else if(note_arr[i].html().length > 150 && (note_arr[i].html()).length <= 250){
				$(note_arr[i]).css('grid-row', (start + ' / ' + (start + 2)));
				$(note_arr[i]).css('min-height', '300px')
			}else{
				$(note_arr[i]).css('grid-row', (start + ' / ' + (start + 2)));
				$(note_arr[i]).css('min-height', '300px')
			}
		}
  }

  $('.burger_button').click(function(){
  	$('.sitebar').toggleClass('sitebar_active')
  })

  $('.note').click(function(){
    id = $(this).attr('value')
    title = $(this).find('h4').html()
    text = $(this).find('input').val()
    $('.popup').append(
    	"<div class='popup_background popup_background_active'></div>"+
			"<div class='popup_exit_button popup_exit_button_active'>"+
				"<span></span>"+
			"</div>").fadeIn(500);
	$('.popup form').append(
    	"<div class='popup_block'>"+
				    "<input type='hidden' name='id' value=" + id + ">"+
					"<input class='title_input' value=" + title + " type='text' name='title'>"+
					"<textarea name='text' id='' cols='30' rows='10'>" + text + "</textarea>"+
					"<div class='buttons_block'>"+
						"<input class='submit_button' type='submit'>"+
					"</div>"+
				"</form>"+
			"</div>"
	).fadeIn(500);
    $(".popup_background").addClass('popup_background_active');
  	$(".popup_exit_button").addClass('popup_exit_button_active');


    $(".popup_exit_button").click(function(){	// Событие клика на затемненный фон
        $(".popup_block").fadeOut(500);	// Медленно убираем всплывающее окно
        $(".popup_background").fadeOut(500);	// Медленно убираем всплывающее окно
        $(".popup_exit_button").fadeOut(500);	// Медленно убираем всплывающее окно
        setTimeout(function() {	// Выставляем таймер
          $(".popup_block").remove();
          $(".popup_background").remove()
        $(".popup_exit_button").remove();
        // Удаляем разметку высплывающего окна
        }, 500);
		});

		$(".popup_background").click(function(){	// Событие клика на затемненный фон
			$(".popup_block").fadeOut(500);	// Медленно убираем всплывающее окно
			$(".popup_background").fadeOut(500);	// Медленно убираем всплывающее окно
			$(".popup_exit_button").fadeOut(500);	// Медленно убираем всплывающее окно
			setTimeout(function() {	// Выставляем таймер
			  $(".popup_block").remove();
			  $(".popup_background").remove()
  			$(".popup_exit_button").remove();
  			// Удаляем разметку высплывающего окна
			}, 500);
		});

		$(document).keyup(function(e) {
   		  if (e.key === "Escape") {
            $(".popup_block").fadeOut(500);	// Медленно убираем всплывающее окно
            $(".popup_background").fadeOut(500);	// Медленно убираем всплывающее окно
            $(".popup_exit_button").fadeOut(500);
            setTimeout(function() {
              $(".popup_block").remove();
              $(".popup_background").remove()
            $(".popup_exit_button").remove();
            }, 500);
   			}
		});
  })

});