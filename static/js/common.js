$(document).ready(function() {
    /* 메뉴오픈 */
    $(document).on('click', '#header .btn-menu', function() {
        if ($('#side-menu').hasClass('active')) {
            $('#side-menu').removeClass('active');
        } else {
            $('#side-menu').addClass('active');
        }
    });
    $(document).on('click', '#header .btn-prev', function() {
        history.back();
    });

    /* 메뉴닫기 */
    $(document).on('click', '#side-menu .close-menu', function() {
        $('#side-menu').removeClass('active');
    });

    /* 메뉴 - profile */
    $(document).on('click', '#side-menu .menu-item.menu-profile', function() {
        location.href = '/profile';
    });

    /* 메뉴 - insight */
    $(document).on('click', '#side-menu .menu-item.menu-insight', function() {
        location.href = '/insight';
    });

    /* 메뉴 - settings */
    $(document).on('click', '#side-menu .menu-item.menu-settings', function() {
        location.href = '/setting';
    });

    /* 메뉴 - logout */
    $(document).on('click', '#side-menu .menu-item.menu-logout', function() {
        location.href = '/logout';
    });
});