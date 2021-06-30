$(document).ready(function(){
	$('#plus-button').click(function() {
		$('#add-note-modal').modal('show');
	});

	$('.note-block').click(function() {
		let title = $(this).find('blockquote p').text();
		let text = $(this).find('blockquote p').text();

		$('#edit-note-modal #note-title').val(title)
		$('#edit-note-modal #note-text').val(text)
		$('#edit-note-modal').modal('show');
	});
});