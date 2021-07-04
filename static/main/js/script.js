$(document).ready(function(){
	$('#plus-button').click(function() {
		$('#add-note-modal').modal('show');
	});

	$('.note-block').click(function() {
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
});