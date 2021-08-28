$(document).ready(function(){
    $(window).scroll(function(){
        let position = $(this).scrollTop();

        if(position >= 80){
            $('.navbar').addClass('fixed-top');
        } else {
            $('.navbar').removeClass('fixed-top');
        }
    })
})