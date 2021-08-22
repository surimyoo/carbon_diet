$(document).ready(function() {
    /* 로그인버튼 */
    $(document).on('click', '.btn-login', function() {
        if ($('#loginForm [name=email]').val() === '') {
            alert('이메일을 입력해주세요.');
            $('#loginForm [name=email]').focus();
            return false;
        }
        if ($('#loginForm [name=password]').val() === '') {
            alert('비밀번호를 입력해주세요.');
            $('#loginForm [name=password]').focus();
            return false;
        }
        $('#loginForm').submit();
    });

    /* 회원가입 버튼 */
    $(document).on('click', '.btn-join', function() {
        location.href = 'join';
    });
	
	$(document).on('keyup', '#loginForm [name=password]', function(e) {
		if (e.keyCode === 13) {
			$('#loginForm .btn-login').trigger('click');
		}
	});
});