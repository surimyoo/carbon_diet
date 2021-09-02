$(document).ready(function() {
    var sec = Math.floor(Math.random() * 3000) + 1500;
    setTimeout(() => {
        $('.waiting-item .waiting-check:eq(0)').addClass('active');
        setTimeout(() => {
            $('.waiting-item .waiting-check:eq(1)').addClass('active');
            setTimeout(() => {
                location.replace('/');
            },1000);
        }, sec);
    }, 1000);
});