window.console = window.console || function() {
   var e = {};
   e.log = e.warn = e.debug = e.info = e.error = e.time = e.dir = e.profile = e.clear = e.exception = e.trace = e.assert = function() {};
   return e
}();

$(document).ready(function() {
	var e = '<div class="switcher-container">'+
                '<h2>STYLE SWITCHER<a href="#" class="switcher-trigger"><i class="fa fa-cog"></i></a></h2>'+'<div class="clearfix"></div>'+
                '<div class="selector">'+
                    '<div class="rtl-layout"><h3>Layout:</h3>'+
                        '<a href="#" class="sw-rtl ttm-btn ttm-btn-size-sm ttm-btn-style-border ttm-btn-color-darkgrey">rtl</a>' +
                        '<a href="#" class="sw-ltr ttm-btn ttm-btn-size-sm ttm-btn-style-border ttm-btn-color-darkgrey">ltr</a>' +
                    '</div>'+ 
                    '<div class="box-layout"><h3>Layout:</h3>'+
                        '<a href="#" class="sw-box ttm-btn ttm-btn-size-sm ttm-btn-style-border ttm-btn-color-darkgrey">box</a>' +
                        '<a href="#" class="sw-wide ttm-btn ttm-btn-size-sm ttm-btn-style-border ttm-btn-color-darkgrey">wide</a>' +
                    '</div>'+                  
                    '<div class="box-pattern"><h3>Background pattern:</h3>'+
                        '<a href="#" data-image="images/pattern/1.png"><img class="img-fluid" src="images/pattern/1.png" alt="image"></a>' +
                        '<a href="#" data-image="images/pattern/2.png"><img class="img-fluid" src="images/pattern/2.png" alt="image"></a>' +
                        '<a href="#" data-image="images/pattern/3.png"><img class="img-fluid" src="images/pattern/3.png" alt="image"></a>' +
                        '<a href="#" data-image="images/pattern/4.png"><img class="img-fluid" src="images/pattern/4.png" alt="image"></a>' +
                        '<a href="#" data-image="images/pattern/5.png"><img class="img-fluid" src="images/pattern/5.png" alt="image"></a>' +
                        '<a href="#" data-image="images/pattern/6.png"><img class="img-fluid" src="images/pattern/6.png" alt="image"></a>' +
                    '</div>'+
                '<div>'+           
                '<div class="clearfix"></div>'+
            '</div>';
	$('body').append(e);
    switchAnimate.loadEvent();
    });

    var switchAnimate = {
        loadEvent: function() {
          $(".switcher-container .switcher-trigger").on('click',function(e) {
            $(this).addClass('active');
             var t = $(".switcher-container");

             if (t.css("left") === "-220px") {
                $(".switcher-container").animate({ left: "0"}, 300, 'easeInOutExpo')
             } else {
                $(this).removeClass('active');
                $(".switcher-container").animate({ left: "-220px" }, 300, 'easeInOutExpo')
             }

             e.preventDefault();
         })
       }
    };