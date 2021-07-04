$(document).ready(function(){
	$('#plus-button').click(function() {
		$('#add-note-modal').modal('show');
	});

	$('.note-block').click(function() {
	    if ($(event.target).attr('class') == 'note-file-block-link') {
	        return
	    }
        $(this).find('#edit-note-modal').modal('show');

        setTimeout(() => {
            let scrollHeight = $('#edit-note-modal #note-text-edit').prop('scrollHeight');
            if (scrollHeight > 300) {
                $(this).find('#note-text-edit').height(scrollHeight)
            }
		}, 170);
	});

	let textarea = $('#note-text-edit');
    textarea.keyup(function() {
        innerHeight = textarea.prop('scrollHeight');
        textarea.height(innerHeight);
    });

    let modal = $('#image-modal');
    let modalImg = $("img#modal-image");
    let modalImgDonwloadLink = $('a#download-modal-image')

    $('.pop-image').on('click', function() {
        let bg = $(this).css('background-image');
        bg = bg.replace('url(','').replace(')','').replace(/\"/gi, "");

        modalImg.attr('src', bg);
        modalImgDonwloadLink.attr('href', bg);
        modalImgDonwloadLink.attr('download', bg);
        modal.addClass('display-block-popup');
    });

    $('.image-modal-background').on('click', function() {
    	if ($(event.target).attr('class') != 'image-modal-background') {
    		return
    	}
    	modal.removeClass('display-block-popup');
    });

});