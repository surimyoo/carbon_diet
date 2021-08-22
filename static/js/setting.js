$(document).ready(function() {
	$(document).on('click', '.setting-list .btn-modify', function() {
		var input = $('.setting-list .setting-' + $(this).data('type'));
		if ($(this).data('type') == 'height') {
			if (input.val() === '') {
				alert('키를 입력하세요.');
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'weight') {
			if (input.val() === '') {
				alert('몸무게를 입력하세요.');
				input.focus();
				return false;
			}
		}

		var param = {
			'type'	: $(this).data('type'),
			'value'	: input.val(),
			'csrfmiddlewaretoken' : $('[name=csrfmiddlewaretoken]').val(),
		};
		$.post('/setting', param, function(response) {
			if (response.result) {
				alert('변경되었습니다.');
			} else {
				if (response.msg) {
					alert(response.msg);
				} else {
					alert('오류가 발생하였습니다.');
				}
			}
		},'json');
	});
});