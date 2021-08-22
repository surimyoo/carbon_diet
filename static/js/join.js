window.onload = function() {
    /* 회원가입 버튼 */
    document.querySelector('.btn-join').addEventListener('click', function() {
        var forms = document.querySelector('#joinForm');

        /* 이름 */
        if (forms.querySelector('[name=name]').value === '') {
            alert('이름을 입력하세요.');
            forms.querySelector('[name=name]').focus();
            return false;
        }
        
        /* 이메일 */
        if (forms.querySelector('[name=email]').value === '') {
            alert('이메일을 입력하세요.');
            forms.querySelector('[name=email]').focus();
            return false;
        }
        var emailExp = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
        if (!forms.querySelector('[name=email]').value.match(emailExp)) {
            alert('이메일 형식이 아닙니다.');
            forms.querySelector('[name=email]').focus();
            return false;
        }
        
        /* 비밀번호 */
        if (forms.querySelector('[name=password]').value === '') {
            alert('비밀번호를 입력하세요.');
            forms.querySelector('[name=password]').focus();
            return false;
        }
        var numExp = /[0-9]/g;
        var engExp = /[a-z]/ig;
        var speExp = /[`~!@@#$%^&*|\\\'\";:\/?]/gi;
        var pwText = forms.querySelector('[name=password]').value;
        if (pwText.length < 8) {
            alert("8자리 이상 입력해주세요.");
            forms.querySelector('[name=password]').focus();
            return false;
        }
		//else if (pwText.search(/\s/) != -1) {
        //    alert("비밀번호는 공백 없이 입력해주세요.");
        //    forms.querySelector('[name=password]').focus();
        //    return false;
        //} else if ((pwText.search(numExp) < 0 && pwText.search(engExp) < 0)
        //            || (pwText.search(numExp) < 0 && pwText.search(speExp) < 0)
        //            || (pwText.search(engExp) < 0 && pwText.search(speExp) < 0)) {
        //    alert("영문,숫자,특수문자 중 2가지 이상을 혼합하여 입력해주세요.");
        //    forms.querySelector('[name=password]').focus();
        //    return false;
        //}

        /* 성별 */
        if (forms.querySelector('[name=gender]:checked') === null) {
            alert('성별을 선택하세요.');
            forms.querySelector('[name=gender]').focus();
            return false;
        }
        
        /* 닉네임 */
        if (forms.querySelector('[name=nick]').value === '') {
            alert('닉네임을 입력하세요.');
            forms.querySelector('[name=nick]').focus();
            return false;
        }
        
        /* 생년월일 */
        if (forms.querySelector('[name=birthday]').value === '') {
            alert('생년월일을 선택하세요.');
            forms.querySelector('[name=birthday]').focus();
            return false;
        }
        
        /* 연락처 */
        if (forms.querySelector('[name=contact]').value === '') {
            alert('전화번호를 입력하세요.');
            forms.querySelector('[name=contact]').focus();
            return false;
        }
        document.querySelector('#joinForm').submit();
    });

	document.querySelectorAll('.btn-radio').forEach(function(e) {
		e.addEventListener('click', function() {
			document.querySelectorAll('.btn-radio').forEach(function(e) {
				e.classList.remove('active');
			});
			this.classList.add('active');
		});
	});
    
    $(document).on('click', '.btn-prev', function() {
        location.href = '/login';
    });
}