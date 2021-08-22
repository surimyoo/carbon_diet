$(document).ready(function() {
    $(document).on('click', '.calendar-item', function() {
        location.href = '?dt=' + $(this).data('day');
    });

    $(document).on('click', '.recipe-item .check-round', function() {
        if ($(this).parent().hasClass('active')) {
            $(this).parent().removeClass('active');
            $(this).parent().find('.is-action').prop('checked', false);
        } else {
            $(this).parent().addClass('active');
            $(this).parent().find('.is-action').prop('checked', true);
        }

		var param = {
			'seq'	: $(this).parent().data('seq'),
            'val'   : $(this).parent().find('.is-action').prop('checked') ? 1 : 0,
			'csrfmiddlewaretoken' : $('[name=csrfmiddlewaretoken]').val(),
		};
		$.post('/planaction', param, function(response) {
		},'json');
    });
    
    $(document).on('click', '.recipe-item .recipe-img', function() {
        location.href = '/recipe?seq=' + $(this).data('seq');
    });
});