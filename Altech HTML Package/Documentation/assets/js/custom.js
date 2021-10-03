$(function() {

  "use strict";

    // Admin panel tab
	$('.themetech-tabs > li > a').on('click', function(e){

    if ( 0 < $(this).next("ul").length ) {
      e.preventDefault();
    }
    
    if ( 0 == $(this).next("ul").length ) {
      return;
    }
	
	if ( $(this).hasClass('open') ) {
	  $(this).removeClass('open').next("ul").slideUp(300);
	  return;
	}
    
    $(this).parents(".themetech-tabs").find("> li > a").removeClass('open');
    $(this).parents(".themetech-tabs").find("ul").not(":hidden").slideUp(300);
    $(this).addClass('open').next("ul").slideDown(300);
  });

  $('.themetech-tabs > li > a.active').addClass('open');
  $('.themetech-tabs > li > ul').prev('a').addClass('has-child');

  // scroll for admin tab
  $('.themetech-tabs.nav a').click(function(){
    $('html, body').animate({scrollTop: $($.attr(this, 'href')).offset().top - 70}, 500);
    return false;
  });

  // Smoothscroll to anchor in page load
  var hash = location.hash.replace('#','');
  if (hash != '' && $("#"+hash).length > 0) {
    $('html, body').animate({scrollTop: $("#"+hash).offset().top-100}, 600);
  }

  if ($(window).height() > $('body').height()) {
    var tm_min_height = $(window).height() - $('.site-header').height() - $('.site-footer').height() - 60;
    $('body > main').css('min-height', tm_min_height);
  }


    //the function is called when the hash changes
  function hashchange(){
    goTo(location.hash, false);
  }
  
  //scroll to a section and set the hash
  function goTo(hash,changehash){
    win.unbind('hashchange', hashchange);
    hash = hash.replace(/!\//,'');
    win.stop().scrollTo(hash,duration,{
      easing:easing,
      axis:'y'      
    });
    if(changehash !== false){
      var l = location;
      location.href = (l.protocol+'//'+l.host+l.pathname+'#!/'+hash.substr(1));
    }
    win.bind('hashchange', hashchange);
  }

  //activate current nav element
  function activateNav(pos){
    var offset = 100,
    current, next, parent, isSub, hasSub;
    win.unbind('hashchange', hashchange);
    for(var i=sectionscount;i>0;i--){
      if(sections[i-1].pos <= pos+offset){
        navanchors.removeClass('current');
        current = navanchors.eq(i-1);
        current.addClass('current');
        
        parent = current.parent().parent();
        next = current.next();
        
        hasSub = next.is('ul');
        isSub = !parent.is('.themetech-tabs');
        
        nav.find('ol:visible').not(parent).slideUp('fast');
        if(isSub){
          parent.prev().addClass('current');
          parent.stop().slideDown('fast');
        }else if(hasSub){
          next.stop().slideDown('fast');
        }
        win.bind('hashchange', hashchange);
        break;
      };
    } 
  }

  // Resposnive Toggle Click
  $('[data-toggle="tm-res-menu"]').on('click', function () {
    $('body').toggleClass('tm-sidebar-open');
    if ($('body').hasClass('tm-sidebar-open')) {
      $('html').css('overflow', 'hidden');
    }
    else {
      $('html').css('overflow', 'visible');
    }
  });


});
