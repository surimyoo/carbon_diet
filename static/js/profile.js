$(document).ready(function() {
	$(document).on('click', '.profile-list .btn-radio', function() {
		$('.profile-list .btn-radio').removeClass('active');
		$(this).addClass('active');
	});
	
	$(document).on('click', '.profile-list .btn-modify', function() {
		var input = $('.profile-list .profile-' + $(this).data('type'));
		if ($(this).data('type') == 'email') {
			if (input.val() === '') {
				alert('이메일을 입력하세요.');
				input.focus();
				return false;
			}
			var emailExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
			if (!input.val().match(emailExp)) {
				alert('이메일 형식이 아닙니다.');
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'name') {
			if (input.val() === '') {
				alert('이름을 입력하세요.');
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'password') {
			if (input.val() === '') {
				alert('비밀번호를 입력하세요.');
				input.focus();
				return false;
			}
			var numExp = /[0-9]/g;
			var engExp = /[a-z]/ig;
			var speExp = /[`~!@@#$%^&*|\\\'\";:\/?]/gi;
			var pwText = input.val();
			if (pwText.length < 8) {
				alert("8자리 이상 입력해주세요.");
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'nick') {
			if (input.val() === '') {
				alert('닉네임을 입력하세요.');
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'birthday') {
			if (input.val() === '') {
				alert('생년월일을 선택하세요.');
				input.focus();
				return false;
			}
		}
		if ($(this).data('type') == 'contact') {
			if (input.val() === '') {
				alert('전화번호를 입력하세요.');
				input.focus();
				return false;
			}
		}

		var param = {
			'type'	: $(this).data('type'),
			'value'	: $(this).data('type') == 'gender' ? $('.profile-list .profile-' + $(this).data('type') + ':checked').val() : input.val(),
			'csrfmiddlewaretoken' : $('[name=csrfmiddlewaretoken]').val(),
		};
		$.post('/profile', param, function(response) {
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