// アコーディオン機能

$(function(){
    $('.js-menu__item__link').each(function(){
        $(this).on('click',function(){
            $("+.submenu",this).slideToggle();
            return false;
        });
    });
});

// ドロワーメニュー機能

$(document).ready(function() {
    $('.drawer').drawer();
});
