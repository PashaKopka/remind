$(document).ready(function(){
	$('#plus-button').click(function() {
		$('#add-note-modal').modal('show');
	});

	$('.note-block').click(function() {
		let title = $(this).find('blockquote p').text().trim();
		let text = $(this).find('figcaption').text().trim();
		let id = $(this).find('input[name="id"]').val();

		$('#edit-note-modal #note-title').val(title);
		$('#edit-note-modal #note-text').val(text);
		$('#edit-note-modal #note-id').val(id);
		$('#edit-note-modal').modal('show');
	});
});