/*
var progressBar = {
	Bar: $("#progress-bar"),
	Reset: function () {
		if (this.Bar) {
			this.Bar.find("li").removeClass("active");
		}
	},
	Next: function () {
		$("#progress-bar li:not(.active):first").addClass("active");
	},
	Back: function () {
		$("#progress-bar li.active:last").removeClass("active");
	}
};

progressBar.Reset();
*/
////

$(document).ready(function() {
    $(document).on('click', '.vegeclass-radio img', function() {
        $(this).parent().find('.vegeclass').prop('checked', true);
        var checkval = $(this).data('val');
        $(this).parent().parent().find('img').each(function(i, v) {
            if ($(this).data('val') >= checkval) {
                $(this).attr('src', $(this).attr('src').replace('non', 'active'));
            } else {$(this).attr('src', $(this).attr('src').replace('active', 'non'));
            }
        });
    });
    
    $(document).on('click', '.btn-question', function() {
        if ($('.question-height').val() == "") {
            alert('키를 입력하세요');
            $('.question-height').focus();
            return false;
        }
        
        if ($('.question-weight').val() == "") {
            alert('몸무게를 입력하세요');
            $('.question-weight').focus();
            return false;
        }
        
        if ($('.vegeclass:checked').length === 0) {
            alert('채식수준을 선택하세요');
            return false;
        }

        param = {
			'csrfmiddlewaretoken' : $('[name=csrfmiddlewaretoken]').val(),
            'height' : $('.question-height').val(),
            'weight' : $('.question-weight').val(),
            'activity' : $('.question-activity').val(),
            'vegeclass' : $('.vegeclass:checked').val(),
            'vegedaily' : $('.question-vegedaily').val(),
            'vegeweekly' : $('.question-vegeweekly').val(),
        };

        $.post('/question', param, function(response) {
            if (response.result) {
                alert('입력이 완료되었습니다.');
                location.href = '/waiting';
            } else {
                alert('입력에 실패하였습니다.\n다시 시도해 주세요.');
            }
        },'json');
    });
})