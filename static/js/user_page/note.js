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
		if (note_arr[i].attr('class') != 'note list'){
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
  }

  $('.burger_button').click(function(){
  	$('.sitebar').toggleClass('sitebar_active')
  })

  $('.note').click(function(){
  if($(event.target).attr('class') == 'note') {
    id = $(this).attr('value')
    title = $(this).find('h4').html()
    text = $(this).find('input').val()
    $('.popup').append(
    	"<div class='popup_background popup_background_active'></div>"+
			"<div class='popup_exit_button popup_exit_button_active'>"+
				"<span></span>"+
			"</div>").fadeIn(500);
	$('.popup #edit_form').append(
    	"<div class='popup_block'>"+
				    "<input type='hidden' name='id' value=" + id + ">"+
					"<input class='title_input' value='" + title + "' type='text' name='title'>"+
					"<textarea name='text' id='' cols='30' rows='10'>" + text + "</textarea>"+
					"<div class='buttons_block'>"+
						"<input value='Save' class='submit_button' type='submit'>"+
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
	}
  })


  $('.add_note_button').click(function(){
    var id = $(this).val()
    $('.popup').append(
    	"<div class='popup_background popup_background_active'></div>"+
			"<div class='popup_exit_button popup_exit_button_active'>"+
				"<span></span>"+
			"</div>").fadeIn(500);
	$('.popup #add_form').append(
    	"<div class='popup_block'>"+
				    "<input class='title_input' placeholder='Title' type='text' name='title'>"+
					"<textarea placeholder='Text' name='text' id='' cols='30' rows='10'></textarea>"+
					"<div class='buttons_block'>"+
						"<input value='Save' class='submit_button' type='submit'>"+
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


  $('.add_note_a').click(function(){
    var id = $(this).val()
    $('.popup').append(
    	"<div class='popup_background popup_background_active'></div>"+
			"<div class='popup_exit_button popup_exit_button_active'>"+
				"<span></span>"+
			"</div>").fadeIn(500);
	$('.popup #add_form').append(
    	"<div class='popup_block'>"+
				    "<input class='title_input' placeholder='Title' type='text' name='title'>"+
					"<textarea placeholder='Text' name='text' id='' cols='30' rows='10'></textarea>"+
					"<div class='buttons_block'>"+
						"<input value='Save' class='submit_button' type='submit'>"+
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


  $('.list').click(function(){
  	if(event.target === this || $(event.target).attr('class') == 'list_item') {
  		var list_item_text_arr = []
  		id = $(this).attr('value')
	    title = $(this).find('h4').html()
	    text = $(this).find('input.hidden_value').val().split('%%_next_%%')
	    $('.popup').append(
	    	"<div class='popup_background popup_background_active'></div>"+
				"<div class='popup_exit_button popup_exit_button_active'>"+
					"<span></span>"+
				"</div>").fadeIn(500);
			$('.popup #edit_form').append(
		    	"<div class='popup_block'>"+
                    "<input type='hidden' name='id' value=" + id + ">"+
                    "<input class='title_input' value='" + title + "' type='text' name='title'>"+
                        "<div class='check_list list_items_block'>"+
                            "<div class='_list_item'>"+
                                "<input class='checkbox' type='checkbox'>"+
                                "<input class='list_item_text' type='text' value=''>"+
                            "</div>"+
    					"</div>"+
							"<input name='list' value='' id='list_input' type='hidden'>"+
							"<div class='buttons_block'>"+
								"<span class='add_list_item'>Add</span>"+
								"<input value='Save' class='submit_button' type='submit'>"+
							"</div>"+
						"</form>"+
					"</div>"
			).fadeIn(500);

		for (var i = 0; i < text.length; i++) {
		    if (text[i] != ''){
		        if (text[i].substr(0, 6) == 'done=0')
                    $('.list_items_block').append(
                        "<div class='_list_item'>"+
                            "<input class='checkbox' type='checkbox'>"+
                            "<input class='list_item_text' type='text' value='" + text[i].substr(6) +"'>"+
                        "</div>"
                    )
                else{
                    $('.list_items_block').append(
                        "<div class='_list_item'>"+
                            "<input class='checkbox' type='checkbox' checked>"+
                            "<input class='list_item_text' type='text' value='" + text[i].substr(6) +"'>"+
                        "</div>"
                    )
                }
            }
        };
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

  	}
  })

  $('.list_item label').click(function(){
  	if ($(this).parent().find('input').is(':checked'))
		{
			$(this).parent().find('input').prop('checked', false);
		}
		else
		{
			$(this).parent().find('input').prop('checked', true);
		}
  })


  $(document).on("click",".submit_button[type='submit']", function(){
    var value = ''
    $('._list_item').each(function(){
        if ($(this).find('.checkbox').is(':checked')){
            value += 'done=1' + $(this).find('.list_item_text').val() + '%%_next_%%'
        }else{
            value += 'done=0' + $(this).find('.list_item_text').val() + '%%_next_%%'
        }
    })
    $('#list_input').val(value)
  });

  $(document).on("click",".add_list_item", function(){
    $('.list_items_block').append(
        "<div class='_list_item'>"+
            "<input class='checkbox' type='checkbox'>"+
            "<input placeholder='your note' class='list_item_text' type='text' value=''>"+
        "</div>"
    )
  })


  $('.add_list_button').click(function(){
	    $('.popup').append(
	    	"<div class='popup_background popup_background_active'></div>"+
				"<div class='popup_exit_button popup_exit_button_active'>"+
					"<span></span>"+
				"</div>").fadeIn(500);
			$('.popup #add_form').append(
		    	"<div class='popup_block'>"+
                    "<input type='hidden' name='id'>"+
                    "<input placeholder='Title' class='title_input' value='' type='text' name='title'>"+
                        "<div class='check_list list_items_block'>"+
                            "<div class='_list_item'>"+
                                "<input class='checkbox' type='checkbox'>"+
                                "<input placeholder='your note' class='list_item_text' type='text' value=''>"+
                            "</div>"+
    					"</div>"+
							"<input name='list' value='' id='list_input' type='hidden'>"+
							"<div class='buttons_block'>"+
								"<span class='add_list_item'>Add</span>"+
								"<input value='Save' class='submit_button' type='submit'>"+
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

  $('.add_list_a').click(function(){
	    $('.popup').append(
	    	"<div class='popup_background popup_background_active'></div>"+
				"<div class='popup_exit_button popup_exit_button_active'>"+
					"<span></span>"+
				"</div>").fadeIn(500);
			$('.popup #add_form').append(
		    	"<div class='popup_block'>"+
                    "<input type='hidden' name='id'>"+
                    "<input placeholder='Title' class='title_input' value='' type='text' name='title'>"+
                        "<div class='check_list list_items_block'>"+
                            "<div class='_list_item'>"+
                                "<input class='checkbox' type='checkbox'>"+
                                "<input placeholder='your note' class='list_item_text' type='text' value=''>"+
                            "</div>"+
    					"</div>"+
							"<input name='list' value='' id='list_input' type='hidden'>"+
							"<div class='buttons_block'>"+
								"<span class='add_list_item'>Add</span>"+
								"<input value='Save' class='submit_button' type='submit'>"+
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